#!/usr/bin/python


ir1b1="""\
 "MCBRDV.4R1.B1"       -151.700000      D2_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MCBRDH.4R1.B1"       -149.800000      D2_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBRD.4L1.B1"         -147.900000      D2_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBRD.4R1.B1"          147.900000      D2_VAL_2      0.000000      0.000000      0.000000      0.000000      0.000000
 "MCBRDH.4R1.B1"        149.800000      D2_VAL_2      0.000000      0.000000      0.000000      0.000000      0.000000
 "MCBRDV.4R1.B1"        151.700000      D2_VAL_2      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXF.4L1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXA.4L1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXA.4R1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXF.4R1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "TAXN.4L1"             999.000000      TAN_VAL_L     TAN_VAL_DL    0.000000      0.000000      0.000000      0.000000
 "TAXN.4R1"             999.000000      TAN_VAL_R     TAN_VAL_DR    0.000000      0.000000      0.000000      0.000000
"""

ir1b1="""\
 "MBRD.4L1.B1"         -147.900000      D2_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBRD.4R1.B1"          147.900000      D2_VAL_2      0.000000      0.000000      0.000000      0.000000      0.000000
 "TCLMA.4L1.B1"         999.900000      D2_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "TCLMA.4R1.B1"         999.000000      D2_VAL_2      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXF.4L1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXA.4L1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXA.4R1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "MBXF.4R1"             999.000000      D1_VAL_1      0.000000      0.000000      0.000000      0.000000      0.000000
 "TAXN.4L1"             999.000000      TAN_VAL_L     TAN_VAL_DL    0.000000      0.000000      0.000000      0.000000
 "TAXN.4R1"             999.000000      TAN_VAL_R     TAN_VAL_DR    0.000000      0.000000      0.000000      0.000000
"""

basedir="/afs/cern.ch/eng/lhc/optics/V6.503/aperture/"

sep=0.194 #separation between apertures Q4/Q5 ...
#sepd2 =0.188; septan=0.160
sepd2 =0.188 #separation between apertures D2
septan=0.145

# septan=0.160
# septan=0.145

#septan1=0.0740*2
#septan2=0.0793*2
septan1=0.158
septan2=0.148
ltan=3.332

#(0.142, 0.164)


repl={
#   'TAN_VAL1':(sep-septan)/2, 'TAN_VAL2':(sep+septan)/2,
   'TAN_VAL_L':(sep-septan1)/2,
   'TAN_VAL_R':(sep+septan2)/2,
   'TAN_VAL_DL':(septan1-septan2)/ltan/2,
   'TAN_VAL_DR':(septan1-septan2)/ltan/2,
   'D2_VAL_1':(sep-sepd2)/2, 'D2_VAL_2':(sep+sepd2)/2,
   'D1_VAL_1': sep/2}

print (septan1-septan2)/ltan/2

for irn in [1,5]:
  for beam in [1,2]:
    fname="offset.ip%d.b%d.tfs"%(irn,beam)
    sign= {1:1,2:-1}[beam]
    st=ir1b1
    for k,v in repl.items():
      st=st.replace(k,'%8.6f'%(sign*v))
    for lr in 'L','R':
      st=st.replace('4%s1'%lr,'4%s%d'%(lr,irn))
      st=st.replace('4%s1.B%d'%(lr,beam),'4%s%d.B%d'%(lr,irn,beam))
    st=open(basedir+fname).read()+st
    print fname
    open(fname,'w').write(st)
