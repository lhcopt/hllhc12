from pyoptics import *

close('all')
#flat and flathv starts from round squeeze
#-> idx=50
#IR2, constraints: 32, variables: 40 (beam1+2)
ds=StrTable.open('../squeeze/ir2_round.tfs')
ds.plot_squeeze()
#fixed
p=ds.poly_fit(ds.get_vars('kq4'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('kq5'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
#not fixed
p=ds.poly_fit(ds.get_vars('kq4.r2b1'),order=4,x0_idx=[39,50,66],xp0_idx=[66,39])
p=ds.poly_fit(ds.get_vars('kq4.r2b1'),order=4,x0_idx=[0,20,39],xp0_idx=[0,39])
p=ds.poly_fit(ds.get_vars('kq5.r2b1'),order=3,x0_idx=[66,50],xp0_idx=[66,50])
p=ds.poly_fit(ds.get_vars('kq5.r2b1'),order=3,x0_idx=[30,0],xp0_idx=[0,30])
p=ds.poly_fit(ds.get_vars('kq5.r2b1'),order=4,x0_idx=[30,40,50],xp0_idx=[30,50])
#IR4, constraints: 14, variable: 18 (per beam)
ds=StrTable.open('../squeeze/ir4_round.tfs')
ds.plot_squeeze()
#fixed
p=ds.poly_fit(ds.get_vars('kq5'),order=5,x0_idx=[66,50,30,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('kq6'),order=5,x0_idx=[66,20,50,0],xp0_idx=[0,66])
#not fixed: kq5.r4b1, kq6.r4b2
#IR6, constraints: 13,variables: 15 (per beam)
#dumxkickb[12]_tcsg is correlated to betxtcdq -> use one of the constraints
ds=StrTable.open('../squeeze/ir6_round.tfs')
#fixed
p=ds.poly_fit(ds.get_vars('dmuxkickb[12]_tcsg'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('dump'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('betytcdq'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('bydumpb1'),order=1,x0_idx=[35,0])
p=ds.poly_fit(ds.get_vars('bydumpb1'),order=4,x0_idx=[66,50,35],xp0_idx=[35,66])
p=ds.poly_fit(ds.get_vars('bydumpb2'),order=6,x0_idx=[66,50,30,10,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('kq4.l6b2'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('kq4.r6b1'),order=7,x0_idx=[66,50,40,30,10,0],xp0_idx=[0,66])#for study_squeeze/squeeze_round/squeeze24/ir6_log_str.tfs use xp0_idx=[1,66]
#not fixed
p=ds.poly_fit(ds.get_vars('kq8.r6b1'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])#for study_squeeze/squeeze_round/squeeze24/ir6_log_str.tfs use xp0_idx=[1,66]
p=ds.poly_fit(ds.get_vars('kq8.r6b2'),order=5,x0_idx=[66,50,20,0],xp0_idx=[0,66])
#IR8, constraints: 28, variables: 40
ds=StrTable.open('../squeeze/ir8_round.tfs')
#fixed
p=ds.poly_fit(ds.get_vars('kq4'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
p=ds.poly_fit(ds.get_vars('kq5'),order=4,x0_idx=[66,50,0],xp0_idx=[0,66])
