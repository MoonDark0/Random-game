import pygame
import turtle
import math
x=0
y=700
z=0
hdir = 0
vdir = 0
dts= 400
Wl=1800
Hl=1000
fps=60
run=True
timer = pygame.time.Clock() 
screen = pygame.display.set_mode((Wl,Hl)) 
color = []
maps=[]
xs = []
ys = []
zs = []
dx = []
dy = []
dz = []
dcol=[]
swap=[]
zbuffer=[]
colorbuffer=[]
events = pygame.event.get()




def start():
    for i in range(0,20):
        for io in range(0,20):
            addcuad(i*500,0,io*500,i*500+500,0,io*500,i*500+500,0,io*500+500,i*500,0,io*500+500,[0,255,0])
            
    prism(-500,500,100,-500,0,100,500,0,100,500,500,100,-500,500,200,-500,0,200,500,0,200,500,500,200,[100,100,100])
    prism(-500,500,1200,-500,0,1200,500,0,1200,500,500,1200,-500,500,1300,-500,0,1300,500,0,1300,500,500,1300,[100,100,100])
    prism(-500,500,100,-500,0,100,-500,0,1300,-500,500,1300,-400,500,100,-400,0,100,-400,0,1300,-400,500,1300,[100,100,100])
    prism(500,500,100,500,0,100,500,0,600,500,500,600,400,500,100,400,0,100,400,0,600,400,500,600,[100,100,100])
    prism(500,500,800,500,0,800,500,0,1300,500,500,1300,400,500,800,400,0,800,400,0,1300,400,500,1300,[100,100,100])
    prism(500,500,600,500,200,600,500,200,800,500,500,800,400,500,600,400,200,600,400,200,800,400,500,800,[100,100,100])
    
    return
def prism(x,y,z,x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4,x5,y5,z5,x6,y6,z6,x7,y7,z7,col):
    addcuad(x,y,z,x1,y1,z1,x2,y2,z2,x3,y3,z3,col)
    addcuad(x,y,z,x1,y1,z1,x5,y5,z5,x4,y4,z4,col)
    addcuad(x,y,z,x3,y3,z3,x7,y7,z7,x4,y4,z4,col)
    addcuad(x6,y6,z6,x2,y2,z2,x3,y3,z3,x7,y7,z7,col)
    addcuad(x6,y6,z6,x2,y2,z2,x1,y1,z1,x5,y5,z5,col)
    addcuad(x6,y6,z6,x7,y7,z7,x4,y,z4,x5,y5,z5,col)
    return
def addcuad(x,y,z,x1,y1,z1,x2,y2,z2,x3,y3,z3,col):
    addtring(x,y,z,x1,y1,z1,x2,y2,z2,col)
    addtring(x,y,z,x2,y2,z2,x3,y3,z3,col)
    return
def addtring(x1,y1,z1,x2,y2,z2,x3,y3,z3,col):
    global xs
    global ys
    global zs
    global color
    xs=xs+[x1, x2, x3]
    ys=ys+[y1, y2, y3]
    zs=zs+[z1, z2, z3]
    color = color+col
    return xs,ys,zs



def frame(xf,yf,zf,xsf,ysf,zsf,hdirf,vdirf,color):
    global dx
    global dy
    global dz
    global Hl
    global Wl
    global zbuffer
    global colorbuffer
    global swap
    global dcol
    dx = []
    dy = []
    dz = []
    relpos(xf,yf,zf,dx,dy,dz,xsf,ysf,zsf)
    dx,dy,dz = rotate(dx,dy,dz,hdirf)
    dx,dy,dz,dcol = render(dx,dy,dz,color)
    dx,dy,dz,dcol,swap=sort(dx,dy,dz,dcol,swap)
    return dx,dy




def relpos(xf,yf,zf,dx,dy,dz,xsf,ysf,zsf):
    i=0
    while i<len(xsf):
        dx.append(xsf[i]-x)
        dy.append(ysf[i]-y)
        dz.append(zsf[i]-z+dts)
        i=i+1
    return dx,dy,dz

def render(dx,dy,dz,color):
    dxt=[]
    dyt=[]
    dct=[]
    dzt=[]
    i=0
    while i<len(dx):
        dct.append(color[i])
        dzt.append(dz[i])
        dxt.append((dx[i]*dts)/dz[i])
        dyt.append((dy[i]*dts)/dz[i])
        i=i+1
    dx=dxt
    dy=dyt
    return dx,dy,dzt,dct
def rotate(dx,dy,dz,hdirf):
    i=0
    dxt = []
    dyt = []
    dzt = []
    hdirrad= hdirf*(math.pi/180)
    while len(dx)>i:
        dxt.append(dx[i]*math.cos(hdirrad)-(dz[i])*math.sin(hdirrad))
        dzt.append(dx[i]*math.sin(hdirrad)+(dz[i])*math.cos(hdirrad))
        i = i+1
    i=0
    dz=[]
    while len(dx)>i:
        dyt.append(dzt[i])
        dz.append(-dy[i])
        i=i+1
    return dxt,dyt,dz

def sort(dx,dy,dz,dcol,swap):
    if len(dx)==0:
        return dx,dy,dz,dcol,swap
    if len(dx)/3==len(swap):
        dxa,dya,dza,dcola=swaplist(dx,dy,dz,dcol,swap)
        if issorted(dza)==1:
            return dxa,dya,dza,dcola,swap
        else:
            cons=len(swap)
            i=0
            swap=[]
            while i<cons:
                swap.append(i)  
                i=i+1
            swap=cleanquicksort(dz,swap)
            dx,dy,dz,dcol=swaplist(dx,dy,dz,dcol,swap)
            return dx,dy,dz,dcol,swap
    else:
        cons=len(dx)
        i=0
        swap=[]
        while i<cons:
            swap.append(i)
            i=i+1
        swap=cleanquicksort(dz,swap)
        dx,dy,dz,dcol=swaplist(dx,dy,dz,dcol,swap)
        return dx,dy,dz,dcol,swap
def issorted(lis):
    leng=len(lis)
    nlis=[]
    i=0
    while i<leng:
        if i%3==0:
            nlis.append(lis)
        i=i+1
    lis=nlis
    leng=len(lis)
    i=0
    rn=lis[i]
    while i<leng:
        if lis[i]>rn:
            rn=lis[i]
        if lis[i]<rn:
            return 0
        i=i+1
    return 1
def cleanquicksort(lis,swap):
    leng=len(lis)
    nlis=[]
    i=0
    while i<leng:
        if i%3==0:
            nlis.append(lis)
        i=i+1
    lis=nlis
    if len(lis)<2:
        return swap
    base=lis[int(len(lis)/2)]
    i=0
    small = []
    big = []
    sswap = []
    baswap = []
    bswap = []
    while i<len(lis):
        if lis[i]<base:
            small.append(lis[i])
            sswap.append(swap[i])
        else:
            if base==lis[i]:
                baswap.append(swap[i])
            else:    
                big.append(lis[i])
                bswap.append(swap[i])
        i=i+1
    return quicksort(small,sswap)+baswap+quicksort(big,bswap)
def quicksort(lis,swap):
    if len(lis)<2:
        return swap
    base=lis[int(len(lis)/2)]
    i=0
    small = []
    big = []
    sswap = []
    baswap = []
    bswap = []
    while i<len(lis):
        if lis[i]<base:
            small.append(lis[i])
            sswap.append(swap[i])
        else:
            if base==lis[i]:
                baswap.append(swap[i])
            else:    
                big.append(lis[i])
                bswap.append(swap[i])
        i=i+1
    return quicksort(small,sswap)+baswap+quicksort(big,bswap)
def swaplist(dx,dy,dz,dcol,swap):
    dxt=[1]*len(swap)*3
    dyt=[1]*len(swap)*3
    dzt=[1]*len(swap)*3
    dcolt=[1]*len(swap)*3
    cons=len(swap)
    i=0
    while i<cons:
        ti=0
        while ti<3:
            ofset=swap[i]*3
            dxt[3*i+ti]=dx[ofset+ti]
            dyt[3*i+ti]=dy[ofset+ti]
            dzt[3*i+ti]=dz[ofset+ti]
            dcolt[3*i+ti]=dcol[ofset+ti]
            ti=ti+1
        i=i+1
    return dxt,dyt,dzt,dcolt




def drsdadaw(px,py,color):
    global Wl
    global Hl
    hHl = Hl/2
    hWl = Wl/2
    i = 0
    lg = len(px)
    while lg>i:
        pygame.draw.polygon(screen,(color[i],color[i+1],color[i+2]),([(px[i]+hWl,-py[i]+hHl),(px[i+1]+hWl,-py[i+1]+hHl),(px[i+2]+hWl,-py[i+2]+hHl)]))
        i=i+3
    return
def draw(px,py,col):
    global Wl
    global Hl
    hHl = Hl/2
    hWl = Wl/2
    i = 0
    lg = len(px)
    while lg>i:
        pygame.draw.line(screen,(color[i],color[i+1],color[i+2]),(px[i]+hWl,-py[i]+hHl),(px[i+1]+hWl,-py[i+1]+hHl))
        pygame.draw.line(screen,(color[i],color[i+1],color[i+2]),(px[i]+hWl,-py[i]+hHl),(px[i+2]+hWl,-py[i+2]+hHl))
        pygame.draw.line(screen,(color[i],color[i+1],color[i+2]),(px[i+2]+hWl,-py[i+2]+hHl),(px[i+1]+hWl,-py[i+1]+hHl))
        i=i+3
    return

start()
frame(x,y,z,xs,ys,zs,hdir,vdir,color)
while run:
    screen.fill((127,210,255))
    timer.tick(fps)
    mpos=pygame.mouse.get_pos()
    draw(dx,dy,dcol)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        z = z+ - 10*math.cos(hdir*(math.pi/180))
        x = x-10*math.sin(hdir*(math.pi/180))
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)
    if keys[pygame.K_w]:
        z = z + 10*math.cos(hdir*(math.pi/180))
        x = x+10*math.sin(hdir*(math.pi/180))
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)
    if keys[pygame.K_LEFT]:
        hdir=(hdir-3)%360
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)
    if keys[pygame.K_RIGHT]:
        hdir=(hdir+3)%360
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)
    if keys[pygame.K_d]:
        x = x+10*math.cos(hdir*(math.pi/180))
        z = z-10*math.sin(hdir*(math.pi/180))
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)
    if keys[pygame.K_a]:
        x = x - 10*math.cos(hdir*(math.pi/180))
        z = z+10*math.sin(hdir*(math.pi/180))
        frame(x,y,z,xs,ys,zs,hdir,vdir,color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.display.update()
