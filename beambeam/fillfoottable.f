c S. Fartoukh 2011/11/16 from SLHCV3.0/beambeam
          program fillfoot
	  implicit none
	  real*8 dQ1,dQ2
	  
	  
	  open(1,file="temp/footprint")
	  open(2,file="temp/fillfoottable.madx")
	  
	  do while(.true.)
	  read(1,*,err=99,end=100) dQ1,dQ2
	  write(2,'(a10,f20.10,a2)') 'dQ1=',dQ1,';'
	  write(2,'(a10,f20.10,a2)') 'dQ2=',dQ2,';'
	  write(2,'(a30,f20.10,a2)') 'fill,table=foottable;'
 99       continue
          enddo
 100      continue
 
          write(2,*)
	  write(2,*) 'return;'
     
         close(1)
	 close(2)
	 
	 stop
	 end
	 
		  
	  
	  
	  
		
		
