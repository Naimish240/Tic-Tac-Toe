from Tkinter import *
import tkMessageBox
import time
import os
import datetime
coun=1
l=[1,2,3,4,5,6,7,8,9] 
#[v1,v2,v3,h1,h2,h3,d1,d2]
hist=[]
cc=[0,0,0,0,0,0,0,0]
oo=[0,0,0,0,0,0,0,0]
fed=0
term=0
root=Tk()
root.update()
C = Canvas(width = 500, height = 300,bg="white")
def mainchoice():
    os.startfile("choice.py")
    root.destroy()
def history():
    global hist
    tkMessageBox.showinfo("History",hist)
def replay():
    global l,cc,oo,fed,coun, hist
    C.delete("all")
    coun=1
    l=[1,2,3,4,5,6,7,8,9]
    cc=[0,0,0,0,0,0,0,0]
    oo=[0,0,0,0,0,0,0,0]
    fed=0
    hist=[]
    C.create_line(100,0, 100, 300, fill="#111111", width=5)
    C.create_line(200, 0, 200, 300, fill="#111111", width=5)
    C.create_line(0,100, 300, 100, fill="#111111", width=5)
    C.create_line(0,200, 300, 200, fill="#111111", width=5)
def save():
    global l,oo,cc,coun
    prev=open("save.txt","w+")
    prev.writelines([str(l),"\n",str(cc),"\n",str(oo),"\n",str(coun)])
    prev.close()
b=Button(root,text="Restart",command=replay)
bs=Button(root,text="Save",command=save)
bc=Button(root,text="Choice",command=mainchoice)
bh=Button(root,text="history",command=history)
def dim():
    global l, term
    if fed==1 or fed==2 or fed==3:
        time.sleep(0.5)
        C.create_rectangle(0,0,300,300,fill="#111111",stipple="gray75")
        root.update()
    if fed==1:
        C.create_text(150,150,text="X wins!",font=("Comic Sans MS", 40),fill="#f20e0e")
        root.update()
        l=list()
        log=open("log3x3.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- X WON \n")
        log.close()
    if fed==2:
        C.create_text(150,150,text="O wins!",font=("Comic Sans MS", 40),fill="#0048ff")
        root.update()
        l=list()
        log=open("log3x3.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- O WON \n")
        log.close()
    if fed==3:
        C.create_text(165,150,text="Draw!",font=("Comic Sans MS", 40),fill="#069631")
        root.update()
        l=list()
        log=open("log3x3.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- DRAW \n")
        log.close()
    if fed==0:
        C.bind('<Button-1>',pritn)
    if fed!=0:
        term=1
        root.quit()
C.pack()
b.pack()
bs.pack()
bc.pack()
bh.pack()
C.create_line(100,0, 100, 300, fill="#111111", width=5)
C.create_line(200, 0, 200, 300, fill="#111111", width=5)
C.create_line(0,100, 300, 100, fill="#111111", width=5)
C.create_line(0,200, 300, 200, fill="#111111", width=5)
def globalize(a,t,lee):
    global coun
    global l,cc,oo,fed
    if a in l:
            l.remove(a)
    coun=coun+1
    if t==0:
        for i in lee:
            oo[i]+=1
    else:
        for i in lee:
            cc[i]+=1
    if 3 in cc:
        fed=1
    if 3 in oo:
        fed=2
    if coun==10 and 3 not in cc and 3 not in oo:
        fed=3
def timer():
    global term
    if term==0:
        for i in range(10,0,-1):
            if term==0:
                ti = C.create_text(400, 100, width=1000000,text=str(i),font=("Comic Sans MS", 60))
                root.update()
                time.sleep(1)
                d=C.create_rectangle(300,0,500,300,fill="white")
                root.update()
                if i==0:
                    tkMessageBox.showinfo("Time's up")
                    root.update()
                    break
                dim()
        else:
            return
def animecirc(cenx,ceny,ee):
    global hist
    hist.append(str(ee)+"-- circle")
    i=0
    while i<=357:
        ext=cenx-46, ceny-46, cenx+46, ceny+46
        C.create_arc(ext,start=0,extent=i,fill="white",outline="red",width=3)
        root.update()
        i+=7
    C.create_rectangle(cenx,ceny-1,cenx+43,ceny+4,fill="white",outline="white")
def animecros(cenx,ceny,ee):
    global hist
    hist.append(str(ee)+"-- cross")
    i=0
    while i<101:
        C.create_line(cenx,ceny,cenx-i,ceny+i,width=3)
        C.create_line(cenx-100,ceny,cenx-100+i,ceny+i,width=3)
        root.update()
        i+=5
def pritn(event):
    ee=0
    t=0
    lee=0
    if coun%2==1:
        
        if((event.x)>=0 and (event.x)<100):
            if ((event.y)>=0 and (event.y)<100)and 1 in l:
                cen1=50
                cen2=50
                ee=1
                lee=[0,3,6]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 2 in l:
                cen1=50
                cen2=150
                ee=2
                lee=[0,4]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 3 in l:
                cen1=50
                cen2=250
                ee=3
                lee=[0,5,7]
                globalize(ee,t,lee)
        if((event.x)>=100 and (event.x)<200):
            if ((event.y)>=0 and (event.y)<100)and 4 in l:
                cen1=150
                cen2=50
                ee=4
                lee=[1,3]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 5 in l:
                cen1=150
                cen2=150
                ee=5
                lee=[1,4,6,7]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 6 in l:
                cen1=150
                cen2=250
                ee=6
                lee=[1,5]
                globalize(ee,t,lee)
        if((event.x)>=200 and (event.x)<300):
            if ((event.y)>=0 and (event.y)<100)and 7 in l:
                cen1=250
                cen2=50
                ee=7
                lee=[2,3,7]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 8 in l:
                cen1=250
                cen2=150
                ee=8
                lee=[2,4]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 9 in l:
                cen1=250
                cen2=250
                ee=9
                lee=[2,5,6]
                globalize(ee,t,lee)
        animecirc(cen1,cen2,ee)
        timer()
    else:
        t=1
        if((event.x)>=0 and (event.x)<100):
            if ((event.y)>=0 and (event.y)<100)and 1 in l:
                cen1=100
                cen2=0
                ee=1
                lee=[0,3,6]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 2 in l:
                cen1=100
                cen2=100
                ee=2
                lee=[0,4]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 3 in l:
                cen1=100
                cen2=200
                ee=3
                lee=[0,5,7]
                globalize(ee,t,lee)
        if((event.x)>=100 and (event.x)<200):
            if ((event.y)>=0 and (event.y)<100)and 4 in l:
                cen1=200
                cen2=0
                ee=4
                lee=[1,3]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 5 in l:
                cen1=200
                cen2=100
                ee=5
                lee=[1,4,6,7]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 6 in l:
                cen1=200
                cen2=200
                ee=6
                lee=[1,5]
                globalize(ee,t,lee)
        if((event.x)>=200 and (event.x)<300):
            if ((event.y)>=0 and (event.y)<100)and 7 in l:
                cen1=300
                cen2=0
                ee=7
                lee=[2,3,7]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 8 in l:
                cen1=300
                cen2=100
                ee=8
                lee=[2,4]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 9 in l:
                cen1=300
                cen2=200
                ee=9
                lee=[2,5,6]
                globalize(ee,t,lee)
        animecros(cen1,cen2,ee)
        timer()
    root.update()
    dim()
dim()
mainloop()
