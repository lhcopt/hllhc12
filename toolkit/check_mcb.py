#!/usr/bin/python

import sys
import gzip
import numpy as np

scale = 23348.89927; #Brho 7 TeV
#dictionary with maximum corrector strength
corrmax= {'acbx%s%s'%(pp,ii): 2.5 for ii in ['1','2'] for pp in ['h','v']}
corrmax.update({'acbx%s3'%(pp): 4.5 for pp in ['h','v']})
corrmax.update({'acbrd%s4'%(pp): 4.5 for pp in ['h','v']})
corrmax.update({'acby%ss4'%(pp): 4.5 for pp in ['h','v']})
#corrmax.update({'acbrd%s4'%(pp): 4.5*1.8/1.5 for pp in ['h','v']})#1.8m length
#corrmax.update({'acby%ss4'%(pp): 4.5*1.8/1.5 for pp in ['h','v']})#1.8m length
corrmax.update({'acby%ss5'%(pp): 2.7 for pp in ['h','v']})
corrmax.update({'acbc%s%s'%(pp,ii): 2.8 for ii in ['6','7'] for pp in ['h','v']})

#dictionary with strength required for IT error correction
iterror= {'acbx%s1'%(pp): 0.92 for pp in ['h','v']}
iterror.update({'acbx%s2'%(pp): 1.40 for pp in ['h','v']})
iterror.update({'acbx%s3'%(pp): 0.78 for pp in ['h','v']})
iterror.update({'acbrd%s4'%(pp): 0.04 for pp in ['h','v']})
iterror.update({'acby%ss4'%(pp): 0.0 for pp in ['h','v']})
iterror.update({'acby%ss5'%(pp): 0.0 for pp in ['h','v']})
iterror.update({'acbc%s%s'%(pp,ii): 0.0 for ii in ['6','7'] for pp in ['h','v']})

#dictionary with strength required for lumi scan knobs
lumi= {'acbx%s1'%(pp): 0.0 for pp in ['h','v']}
lumi.update({'acbx%s2'%(pp): 0.0 for pp in ['h','v']})
lumi.update({'acbx%s3'%(pp): 0.0 for pp in ['h','v']})
lumi.update({'acbrd%s4'%(pp): 0.27 for pp in ['h','v']})
lumi.update({'acby%ss4'%(pp): 0.20 for pp in ['h','v']})
lumi.update({'acby%ss5'%(pp): 0.0 for pp in ['h','v']})
lumi.update({'acbc%s%s'%(pp,ii): 0.0 for ii in ['6','7'] for pp in ['h','v']})

#dictionary with strength required for correction of arc imperfections scan knobs
arc= {'acbx%s1'%(pp): 0.0 for pp in ['h','v']}
arc.update({'acbx%s2'%(pp): 0.0 for pp in ['h','v']})
arc.update({'acbx%s3'%(pp): 0.0 for pp in ['h','v']})
arc.update({'acbrd%s4'%(pp): 0.0 for pp in ['h','v']})
arc.update({'acby%ss4'%(pp): 0.7 for pp in ['h','v']})
arc.update({'acby%ss5'%(pp): 0.0 for pp in ['h','v']})
arc.update({'acbc%s%s'%(pp,ii): 0.0 for ii in ['6','7'] for pp in ['h','v']})

#dictionary with strength required for D2 transfer fucntion errors scan knobs
#assume 2.e-3 transfer function error for 35 Tm
d2err=35*2.e-3
d2trans= {'acbx%s1'%(pp): 0.0 for pp in ['h','v']}
d2trans.update({'acbx%s2'%(pp): 0.0 for pp in ['h','v']})
d2trans.update({'acbx%s3'%(pp): 0.0 for pp in ['h','v']})
d2trans.update({'acbrd%s4'%(pp): d2err for pp in ['h','v']})
d2trans.update({'acby%ss4'%(pp): 0.0 for pp in ['h','v']})
d2trans.update({'acby%ss5'%(pp): 0.0 for pp in ['h','v']})
d2trans.update({'acbc%s%s'%(pp,ii): 0.0 for ii in ['6','7'] for pp in ['h','v']})

fixedmargins=[iterror,arc,d2trans,lumi]

def mk_dic(fn): 
  """create dictionary from mad output file"""
  corrs={}
  if fn.endswith('.gz'):
    fh=gzip.open(fn)
  else:
    fh=file(fn)
  for l in fh:
    [name,acb]=l.replace(' ','').replace(';','').split('=')
    corrs[name]=float(acb)
  return corrs

def print_acb(corrs,name,scale = 23348.89927):
  out=[name]
  tot=0
  for pp in ['x','s','o','ccp','ccm','ccs']:
    out.append(scale*corrs[name+pp])
  #iterror+lumiscan
  for err in fixedmargins:
    out.append(err[name.split('.')[0]])
  #--calculate total strength
  tot = scale*max(abs(corrs[name+'x']),abs(corrs[name+'s']))
  #add contribution from other knobs
  for pp in ['o','ccp','ccm','ccs']:
    tot=tot+scale*abs(corrs[name+pp])
  for err in fixedmargins:
    tot = tot+abs(err[name.split('.')[0]])#add strength necessary for IT error correction
  out.append(tot)
  #maximum and margin
  cmax=corrmax[name.split('.')[0]]
  out.append(cmax)
  margin=(cmax-tot)*100/cmax
  out.append(margin)
  print ('%-15s'+'%7.2f'*13) % tuple(out)
  return out

def check_orbit(fn):
  print "Checking %s" % fn
  print "for 'tot' use maximum value over 'x' and 's'"
  corrs=mk_dic(fn)
  print('%50s') % ('corrector strength [Tm]')
  print('%-18s'+' %-6s'*13) % ('name','x','s','o','ccp','ccm','ccs','iterror','arc','d2trans','lumi','tot','max','margin [%]')
  outall=[]#list to save the maximum values in for the summary table
  for cc,ii in zip(['acbx','acbx','acbx','acbrd','acby','acby','acbc','acbc'],['1','2','3','4','s4','s5','6','7']): 
    outallmax=[]
    outmargin=[]
    for pp in 'h','v':
      for ss in 'l','r':
        for ip in '1','5':
          if cc == 'acbx':
            name='%s%s%s.%s%s'%(cc,pp,ii,ss,ip)
            out=print_acb(corrs,name)
            outallmax.append(out[1:-1])#maximum strength
            outmargin.append([out[-1]])
          else:
            for bb in 'b1','b2':
              name='%s%s%s.%s%s%s'%(cc,pp,ii,ss,ip,bb)
              if name+'x' in corrs.keys():
                out=print_acb(corrs,name)
                outallmax.append([abs(ll) for ll in out[1:-1] ])#maximum strength
                outmargin.append([out[-1]])
    #get the maximum,use numpy method in order to define the axis
    maxall=list(np.max(np.array(outallmax),axis=0))
    marginall=[np.min(np.array(outmargin))]
    sout=(('-- '+name.split('.')[0].replace('v','[hv]')).ljust(15)+'%7.2f'*13) % tuple(maxall+min(outmargin))
    outall.append([sout])
    print sout
  print 'Summary table'
  print('%50s') % ('corrector strength [Tm]')
  print('%-18s'+' %-6s'*13) % ('name','x','s','o','ccp','ccm','ccs','iterror','arc','d2trans','lumi','tot','max','margin [%]')
  for ll in outall:
    print '%s'%(ll[0])

check_orbit(sys.argv[1])
