#!/usr/bin/python

import sys
import gzip
import os

labels=['NAME', 'BETX', 'BETY', 'DX', 'X', 'Y', 'N1']

def check_aperture(fn):
  print "%s" % fn,
  if fn.endswith('.gz'):
    fh=gzip.open(fn)
  else:
    fh=file(fn)

  idx={}   #associate a column name to a column index

  out=[]
  n1min=99999
  for l in fh:
    if l.startswith('*'):
      label_line=l.split()
      for lb in labels:
        idx[lb]=label_line.index(lb)-1
    elif l.startswith(' '):
      data=l.split()
      name,betx,bety,dx,x,y,n1=[ eval(data[idx[lb]]) for lb in labels]
      if name.startswith('M'):
        if n1min>n1:
          namemin=name
          n1min=n1
  return namemin,n1min

basedir=sys.argv[1]

for beam in [1,2]:
  for ir in [1,5]:
    fn=os.path.join(basedir,"ap_ir%db%d.tfs.gz"%(ir,beam))
    name,n1=check_aperture(fn)
    print "%-30s %5.2f"%(name,n1)
