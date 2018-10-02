            program headonslice
	    
	    implicit none
	    integer Nmax
	    parameter(Nmax=100)
	    real*8 ractwopi
	    common/cst/ractwopi
	    real*8 x,myerf,arcerf
	    real*8 long(0:Nmax)
	    character*12 charslice(4,0:Nmax)
	    integer NIR1,NIR2,NIR5,NIR8
	    integer is
	    
	    ractwopi=sqrt(4.0d0*asin(1.0d0))
	    
	    call formchar(charslice)
	    
	    open(1,file="temp/sliceho.input")
	    read(1,*) NIR1
	    read(1,*) NIR2
	    read(1,*) NIR5
	    read(1,*) NIR8
	    close(1)
	    NIR1=(NIR1)/2
	    NIR2=(NIR2)/2
	    NIR5=(NIR5)/2
	    NIR8=(NIR8)/2
	    if(NIR1.lt.0.or.NIR1.gt.Nmax) then
	    write(6,*) "Bad number of ho slice in IR1"
	    stop
	    endif
	    if(NIR2.lt.0.or.NIR2.gt.Nmax) then
	    write(6,*) "Bad number of ho slice in IR2"
	    stop
	    endif
	    if(NIR5.lt.0.or.NIR5.gt.Nmax) then
	    write(6,*) "Bad number of ho slice in IR5"
	    stop
	    endif
	    if(NIR8.lt.0.or.NIR8.gt.Nmax) then
	    write(6,*) "Bad number of ho slice in IR8"
	    stop
	    endif
	    
	    
	    open(1,file="temp/sliceho.madx")
	    call slice(NIR1,long)
	    write(1,*) "!*****IR1*****"
	    write(1,'(a12,a4,2x,e14.6,a14)')
     +   "hocharge_IR1"," := ",1.0d0/(2.0d0*NIR1+1.0d0)," * ho_charge ;" 
	    do is=1,NIR1
	    write(1,'(a12,a4,2x,f9.3,a12)')
     +      charslice(1,is)," := ",long(is)," * sigz/2 ;"
	    enddo
	    write(1,*) 
	    call slice(NIR2,long)
	    write(1,*) "!*****IR2*****"
	    write(1,'(a12,a4,2x,e14.6,a14)')
     +   "hocharge_IR2"," := ",1.0d0/(2.0d0*NIR2+1.0d0)," * ho_charge ;" 
	    do is=1,NIR2
	    write(1,'(a12,a4,2x,f9.3,a12)')
     +      charslice(2,is)," := ",long(is)," * sigz/2 ;"
	    enddo
	    write(1,*) 
	    call slice(NIR5,long)
	    write(1,*) "!*****IR5*****"
	    write(1,'(a12,a4,2x,e14.6,a14)')
     +   "hocharge_IR5"," := ",1.0d0/(2.0d0*NIR5+1.0d0)," * ho_charge ;" 
	    do is=1,NIR5
	    write(1,'(a12,a4,2x,f9.3,a12)')
     +      charslice(3,is)," := ",long(is)," * sigz/2 ;"
	    enddo
	    write(1,*) 
	    call slice(NIR8,long)
	    write(1,*) "!*****IR8*****"
	    write(1,'(a12,a4,2x,e14.6,a14)')
     +   "hocharge_IR8"," := ",1.0d0/(2.0d0*NIR8+1.0d0)," * ho_charge ;" 
	    do is=1,NIR8
	    write(1,'(a12,a4,2x,f9.3,a12)')
     +      charslice(4,is)," := ",long(is)," * sigz/2 ;"
	    enddo
	    write(1,*) 
	    write(1,*) 
	    write(1,*) "value,hocharge_IR1;"
	    do is=1,NIR1
	    write(1,*) "value,",charslice(1,is),";"
	    enddo
	    write(1,*) 
	    write(1,*) "value,hocharge_IR2;"
	    do is=1,NIR2
	    write(1,*) "value,",charslice(2,is),";"
	    enddo
	    write(1,*) 
	    write(1,*) "value,hocharge_IR5;"
	    do is=1,NIR5
	    write(1,*) "value,",charslice(3,is),";"
	    enddo
	    write(1,*) 
	    write(1,*) "value,hocharge_IR8;"
	    do is=1,NIR8
	    write(1,*) "value,",charslice(4,is),";"
	    enddo
	    write(1,*)	    
	    write(1,*) "return;"
	    
	    stop
	    end
	    
	    
	    function myerf(x)
	    
	    implicit none
	    real*8 x,myerf
	    
	    real*8 eps,GCUT
	    parameter(eps=1.d-10,GCUT=7.0d0)
	    
	    real*8 ractwopi
	    common/cst/ractwopi
	    
	    real*8  aux,x2s2
	    integer i,Nx
	    
	    if(x.gt.GCUT) then
	    write(6,*) 'Error in argument of myerf'
	    stop
	    endif
	    
	    aux=x
	    x2s2=x*x/2.d0
	    myerf=x
	    Nx=NINT(abs(x))
	    i=1
	    do while(abs(aux).gt.eps.or.i.le.Nx)
	    aux=-aux*x2s2/i
	    myerf=myerf+aux/(2.0d0*i+1.0d0)
	    i=i+1
	    enddo
	    
	    myerf=myerf/ractwopi
	    
	    return
	    end
	    
	    
	    function arcerf(y)
	    
	    implicit none	    
	    real*8 y,arcerf
	    
	    real*8 eps,GCUT
	    parameter(eps=1.d-6,GCUT=7.0d0)
	    
	    real*8 ractwopi
	    common/cst/ractwopi
	    
	    real*8 yaux,ymax,ymin,ymid,xmax,xmin,xmid,myerf
	    integer i,Nx
	    
	    yaux=abs(y)
	    if(yaux.ge.0.499999d0) then
	    write(6,*) 'Error in argument of arcmyerf'
	    stop
	    endif
	    
	    xmin=0.d0
	    xmax=GCUT
	    xmid=xmin+(xmax-xmin)*0.5d0
	    ymid=myerf(xmid)
	    do while(abs(ymid-yaux).gt.eps)
	    if(ymid.gt.y) xmax=xmid
	    if(ymid.lt.y) xmin=xmid
	    xmid=xmin+(xmax-xmin)*0.5d0
	    ymid=myerf(xmid)
	    enddo
	    
	    arcerf=xmid
	    
	    return
	    end
	    
	    function bari(y1,y2)
	    
	    implicit none
	    
	    real*8 bari,y1,y2
	    real*8 ractwopi
	    common/cst/ractwopi
	    real*8 x1,x2,arcerf
	    x1=arcerf(y1)
	    x2=arcerf(y2)
	    bari=abs(exp(-x1*x1*0.5d0)-exp(-x2*x2*0.5d0))/
     +            ractwopi/(y2-y1)
	    
	    return
	    end
	    
	    subroutine slice(N,long)
	    
	    implicit none
	    integer Nmax
	    parameter(Nmax=100)
	    real*8 ractwopi
	    common/cst/ractwopi
	    integer N,is
	    real*8 long(0:Nmax),hocharge,y1,y2,arcerf,bari,x1
	    real*8 aux	    
	    
	    if(N.gt.Nmax) then
	    write(6,*) "Too many ho slices requested!"
	    stop
	    endif
	    if(N.lt.0) then
	    write(6,*) "Negative number of ho slices requested!"
	    stop
	    endif
	    
	    do is=0,Nmax
	    long(is)=0.d0
	    enddo
	    
	    long(0)=0.d0
	    if(N.eq.0) return
	    hocharge=1.d0/(2.0*N+1.0d0)
	    y1=hocharge*0.5d0
	    y2=y1+hocharge
	    do is=1,N-1
	    long(is)=bari(y1,y2)
	    y1=y2
	    y2=y2+hocharge
	    enddo
	    x1=arcerf(y1)
	    long(N)=exp(-x1*x1*0.5d0)/hocharge/ractwopi
	    
	    aux=0.
	    do is=0,N
	    aux=aux+long(is)**2*hocharge
	    enddo
	      
	    return
	    end
	    
	    subroutine formchar(charslice)
	    
	    implicit none
	    integer Nmax
	    parameter(Nmax=100)
	    character*12 charslice(4,0:Nmax)
	    character*3 charaux(0:Nmax)
	    integer i,j
	    
	    charaux(  0)=  "0"
	    charaux(  1)=  "1"
	    charaux(  2)=  "2"
	    charaux(  3)=  "3"
	    charaux(  4)=  "4"
	    charaux(  5)=  "5"
	    charaux(  6)=  "6"
	    charaux(  7)=  "7"
	    charaux(  8)=  "8"
	    charaux(  9)=  "9"
	    charaux( 10)= "10"
	    charaux( 11)= "11"
	    charaux( 12)= "12"
	    charaux( 13)= "13"
	    charaux( 14)= "14"
	    charaux( 15)= "15"
	    charaux( 16)= "16"
	    charaux( 17)= "17"
	    charaux( 18)= "18"
	    charaux( 19)= "19"
	    charaux( 20)= "20"
	    charaux( 21)= "21"
	    charaux( 22)= "22"
	    charaux( 23)= "23"
	    charaux( 24)= "24"
	    charaux( 25)= "25"
	    charaux( 26)= "26"
	    charaux( 27)= "27"
	    charaux( 28)= "28"
	    charaux( 29)= "29"
	    charaux( 30)= "30"
	    charaux( 31)= "31"
	    charaux( 32)= "32"
	    charaux( 33)= "33"
	    charaux( 34)= "34"
	    charaux( 35)= "35"
	    charaux( 36)= "36"
	    charaux( 37)= "37"
	    charaux( 38)= "38"
	    charaux( 39)= "39"
	    charaux( 40)= "40"
	    charaux( 41)= "41"
	    charaux( 42)= "42"
	    charaux( 43)= "43"
	    charaux( 44)= "44"
	    charaux( 45)= "45"
	    charaux( 46)= "46"
	    charaux( 47)= "47"
	    charaux( 48)= "48"
	    charaux( 49)= "49"
	    charaux( 50)= "50"
	    charaux( 51)= "51"
	    charaux( 52)= "52"
	    charaux( 53)= "53"
	    charaux( 54)= "54"
	    charaux( 55)= "55"
	    charaux( 56)= "56"
	    charaux( 57)= "57"
	    charaux( 58)= "58"
	    charaux( 59)= "59"
	    charaux( 60)= "60"
	    charaux( 61)= "61"
	    charaux( 62)= "62"
	    charaux( 63)= "63"
	    charaux( 64)= "64"
	    charaux( 65)= "65"
	    charaux( 66)= "66"
	    charaux( 67)= "67"
	    charaux( 68)= "68"
	    charaux( 69)= "69"
	    charaux( 70)= "70"
	    charaux( 71)= "71"
	    charaux( 72)= "72"
	    charaux( 73)= "73"
	    charaux( 74)= "74"
	    charaux( 75)= "75"
	    charaux( 76)= "76"
	    charaux( 77)= "77"
	    charaux( 78)= "78"
	    charaux( 79)= "79"
	    charaux( 80)= "80"
	    charaux( 81)= "81"
	    charaux( 82)= "82"
	    charaux( 83)= "83"
	    charaux( 84)= "84"
	    charaux( 85)= "85"
	    charaux( 86)= "86"
	    charaux( 87)= "87"
	    charaux( 88)= "88"
	    charaux( 89)= "89"
	    charaux( 90)= "90"
	    charaux( 91)= "91"
	    charaux( 92)= "92"
	    charaux( 93)= "93"
	    charaux( 94)= "94"
	    charaux( 95)= "95"
	    charaux( 96)= "96"
	    charaux( 97)= "97"
	    charaux( 98)= "98"
	    charaux( 99)= "99"
	    charaux(100)="100"
	    
	    do i=0,Nmax
	    charslice(1,i)="long_IR1_"//charaux(i)
	    enddo
	    do i=0,Nmax
	    charslice(2,i)="long_IR2_"//charaux(i)
	    enddo
	    do i=0,Nmax
	    charslice(3,i)="long_IR5_"//charaux(i)
	    enddo
	    do i=0,Nmax
	    charslice(4,i)="long_IR8_"//charaux(i)
	    enddo
	    
	    return
	    end
	    
	    
	   
	    
	    
