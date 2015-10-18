from pyoptics import *

close('all')
#--- compare new/old squeeze
def plot_squeeze_diff(ir='2468',opt='round'):
  for i in ir:
    ds=StrTable.open('ir%s_%s.tfs'%(i,opt))
    ds.plot_squeeze_diff(fn='ir%s_log_str.tfs'%i,title='comp squeeze IR%s'%i)
    dsnew=StrTable.open('ir%s_log_str.tfs'%i)
    print i,max(dsnew['tarir%sb1'%i]),max(dsnew['tarir%sb2'%i])
def plot_squeeze(ir='2468',opt='round'):
  close('all')
  for i in ir:
    ds=StrTable.open('ir%s_%s.tfs'%(i,opt))
    ds.plot_squeeze(title='squeeze IR%s'%i)
    print i,max(ds['tarir%sb1'%i]),max(ds['tarir%sb2'%i])
    savefig('ir%s_%s.png'%(i,opt))

for opt in 'round','flat','flathv':
  figure(opt)
  ds=StrTable.open('ir6_%s.tfs'%opt)
  plot(ds.betxtcdsb1,'k',label='betx TCDS.A*.B1')
  plot(ds.betytcdsb1,'r',label='bety TCDS.A*.B1')
  plot(ds.betxtcdsb2,'b',label='betx TCDS.A*.B2')
  plot(ds.betytcdsb2,'m',label='bety TCDS.A*.B2')
  xlabel(r'squeeze step (squeeze -> presqueeze)')
  ylabel(r'$\beta_{x/y,\rm TCDS.A}$ [m]')
  title('%s squeeze'%opt)
  legend(loc='best')
  savefig('ir6_%s_beta_tcsg.png'%(opt))

plot_squeeze_diff(opt='round')
plot_squeeze_diff(opt='flat')
plot_squeeze_diff(opt='flathv')
plot_squeeze(opt='round')
plot_squeeze(opt='flat')
plot_squeeze(opt='flathv')
