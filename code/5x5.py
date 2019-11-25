from Tkinter import *
import time
import os
import datetime
coun=1
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25] 
#[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, da1,da2,da3,da4, db1,db2,db3,db4]
cc=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
oo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
fed=0
root=Tk()
C = Canvas(width = 500, height = 500,bg="white")
def mainchoice():
    os.startfile("choice.py")
    root.destroy()
def replay():
    global l,cc,oo,fed,coun
    C.delete("all")
    coun=1
    l=[1,2,3,4,5,6,7,8,9.10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    cc=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    oo=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fed=0
    C.create_line(100,0, 100, 500, fill="#111111", width=5)
    C.create_line(200, 0, 200, 500, fill="#111111", width=5)
    C.create_line(300,0, 300, 500, fill="#111111", width=5)
    C.create_line(400, 0, 400, 500, fill="#111111", width=5)
    C.create_line(0,100, 500, 100, fill="#111111", width=5)
    C.create_line(0,200, 500, 200, fill="#111111", width=5)
    C.create_line(0,300, 500, 300, fill="#111111", width=5)
    C.create_line(0,400, 500, 400, fill="#111111", width=5)
b=Button(root,text="Restart",command=replay)
bc=Button(root,text="Choice",command=mainchoice)
def dim():
    global l
    if fed==1 or fed==2 or fed==3:
        time.sleep(0.5)
        C.create_rectangle(0,0,500,500,fill="#111111",stipple="gray75")
        root.update()
    if fed==1:
        C.create_text(250,250,text="X wins!",font=("Comic Sans MS", 40),fill="#f20e0e")
        root.update()
        log=open("log5x5.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- X WON \n")
        log.close()
        l=list()
    if fed==2:
        C.create_text(250,250,text="O wins!",font=("Comic Sans MS", 40),fill="#0048ff")
        root.update()
        log=open("log5x5.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- O WON \n")
        log.close()
        l=list()
    if fed==3:
        C.create_text(265,250,text="Draw!",font=("Comic Sans MS", 40),fill="#069631")
        root.update()
        log=open("log5x5.txt","a")
        log.writelines(str(datetime.datetime.now())[:16]+"- DRAW \n")
        log.close()
        l=list()
    if fed==0:
        C.bind('<Button-1>',pritn)
C.pack()
b.pack()
bc.pack()
C.create_line(100,0, 100, 500, fill="#111111", width=5)
C.create_line(200, 0, 200, 500, fill="#111111", width=5)
C.create_line(300,0, 300, 500, fill="#111111", width=5)
C.create_line(400, 0, 400, 500, fill="#111111", width=5)
C.create_line(0,100, 500, 100, fill="#111111", width=5)
C.create_line(0,200, 500, 200, fill="#111111", width=5)
C.create_line(0,300, 500, 300, fill="#111111", width=5)
C.create_line(0,400, 500, 400, fill="#111111", width=5)
def globalize(a,t,lee):
    global coun,oo,cc
    global l,fed
    if a in l:
            l.remove(a)
    coun=coun+1
    if t==0:
        for i in lee:
            oo[i]+=1
    else:
        for i in lee:
            cc[i]+=1
    if 4 in cc:
        fed=1
    if 4 in oo:
        fed=2
    if coun==26 and 4 not in cc and 4 not in oo:
        fed=3
def animecirc(cenx,ceny):
    i=0
    while i<=357:
        ext=cenx-46, ceny-46, cenx+46, ceny+46
        C.create_arc(ext,start=0,extent=i,fill="white",outline="red",width=3)
        root.update()
        i+=7
    C.create_rectangle(cenx,ceny-1,cenx+43,ceny+4,fill="white",outline="white")
def animecros(cenx,ceny):
    i=0
    cenx+=50
    ceny-=50
    while i<101:
        C.create_line(cenx,ceny,cenx-i,ceny+i,width=3)
        C.create_line(cenx-100,ceny,cenx-100+i,ceny+i,width=3)
        root.update()
        i+=10
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
                lee=[0, 10, 20] #correct
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 2 in l:
                cen1=50
                cen2=150
                ee=2
                lee=[0, 5, 11, 23] #correct
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 3 in l:
                cen1=50
                cen2=250
                ee=3
                lee=[0,5,12] #correct
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 4 in l:
                cen1=50
                cen2=350
                ee=4
                lee=[0,5,13,26]#correct
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 5 in l:
                cen1=50
                cen2=450
                ee=5
                lee=[5,14,25]#correct
                globalize(ee,t,lee)
        if((event.x)>=100 and (event.x)<200):
            if ((event.y)>=0 and (event.y)<100)and 6 in l:
                cen1=150
                cen2=50
                ee=6
                lee=[1,10,15,22]#correct
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 7 in l:
                cen1=150
                cen2=150
                ee=7
                lee=[1,6,11,16,20,21]#correct
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 8 in l:
                cen1=150
                cen2=250
                ee=8
                lee=[1,6,12,17,23,26]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 9 in l:
                cen1=150
                cen2=350
                ee=9
                lee=[1,6,13,18,24,25]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 10 in l:
                cen1=150
                cen2=450
                ee=10
                lee=[6,14,19,27]
                globalize(ee,t,lee)
        if((event.x)>=200 and (event.x)<300):
            if ((event.y)>=0 and (event.y)<100)and 11 in l:
                cen1=250
                cen2=50
                ee=11
                lee=[2,10,15]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 12 in l:
                cen1=250
                cen2=150
                ee=12
                lee=[2,7,11,16,22,26]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 13 in l:
                cen1=250
                cen2=250
                ee=13
                lee=[2, 7, 12, 17, 20, 21, 24, 25]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 14 in l:
                cen1=250
                cen2=350
                ee=14
                lee=[2, 7, 13, 18, 23, 27]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 15 in l:
                cen1=250
                cen2=450
                ee=15
                lee=[7,14,19]
                globalize(ee,t,lee)
        if((event.x)>=300 and (event.x)<400):
            if ((event.y)>=0 and (event.y)<100)and 16 in l:
                cen1=350
                cen2=50
                ee=16
                lee=[3,10,15,26]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 17 in l:
                cen1=350
                cen2=150
                ee=17
                lee=[3,8,11,16,24,25]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 18 in l:
                cen1=350
                cen2=250
                ee=18
                lee=[3,8,12,17,22,27]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 19 in l:
                cen1=350
                cen2=350
                ee=19
                lee=[3,8,13,18,20,21]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 20 in l:
                cen1=350
                cen2=450
                ee=20
                lee=[8,14,19,23]
                globalize(ee,t,lee)
        if((event.x)>=400 and (event.x)<500):
            if ((event.y)>=0 and (event.y)<100)and 21 in l:
                cen1=450
                cen2=50
                ee=21
                lee=[4,15,24]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 22 in l:
                cen1=450
                cen2=150
                ee=22
                lee=[4,9,16,27]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 23 in l:
                cen1=450
                cen2=250
                ee=23
                lee=[4, 9, 17]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 24 in l:
                cen1=450
                cen2=350
                ee=24
                lee=[4,9,18,22]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 25 in l:
                cen1=450
                cen2=450
                ee=25
                lee=[9,19,21]
                globalize(ee,t,lee)
        animecirc(cen1,cen2)
    else:
        t=1
        if((event.x)>=0 and (event.x)<100):
            if ((event.y)>=0 and (event.y)<100)and 1 in l:
                cen1=50
                cen2=50
                ee=1
                lee=[0, 10, 20] #correct
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 2 in l:
                cen1=50
                cen2=150
                ee=2
                lee=[0, 5, 11, 23] #correct
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 3 in l:
                cen1=50
                cen2=250
                ee=3
                lee=[0,5,12] #correct
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 4 in l:
                cen1=50
                cen2=350
                ee=4
                lee=[0,5,13,26]#correct
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 5 in l:
                cen1=50
                cen2=450
                ee=5
                lee=[5,14,25]#correct
                globalize(ee,t,lee)
        if((event.x)>=100 and (event.x)<200):
            if ((event.y)>=0 and (event.y)<100)and 6 in l:
                cen1=150
                cen2=50
                ee=6
                lee=[1,10,15,22]#correct
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 7 in l:
                cen1=150
                cen2=150
                ee=7
                lee=[1,6,11,16,20,21]#correct
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 8 in l:
                cen1=150
                cen2=250
                ee=8
                lee=[1,6,12,17,23,26]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 9 in l:
                cen1=150
                cen2=350
                ee=9
                lee=[1,6,13,18,24,25]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 10 in l:
                cen1=150
                cen2=450
                ee=10
                lee=[6,14,19,27]
                globalize(ee,t,lee)
        if((event.x)>=200 and (event.x)<300):
            if ((event.y)>=0 and (event.y)<100)and 11 in l:
                cen1=250
                cen2=50
                ee=11
                lee=[2,10,15]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 12 in l:
                cen1=250
                cen2=150
                ee=12
                lee=[2,7,11,16,22,26]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 13 in l:
                cen1=250
                cen2=250
                ee=13
                lee=[2, 7, 12, 17, 20, 21, 24, 25]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 14 in l:
                cen1=250
                cen2=350
                ee=14
                lee=[2, 7, 13, 18, 23, 27]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 15 in l:
                cen1=250
                cen2=450
                ee=15
                lee=[7,14,19]
                globalize(ee,t,lee)
        if((event.x)>=300 and (event.x)<400):
            if ((event.y)>=0 and (event.y)<100)and 16 in l:
                cen1=350
                cen2=50
                ee=16
                lee=[3,10,15,26]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 17 in l:
                cen1=350
                cen2=150
                ee=17
                lee=[3,8,11,16,24,25]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 18 in l:
                cen1=350
                cen2=250
                ee=18
                lee=[3,8,12,17,22,27]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 19 in l:
                cen1=350
                cen2=350
                ee=19
                lee=[3,8,13,18,20,21]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 20 in l:
                cen1=350
                cen2=450
                ee=20
                lee=[8,14,19,23]
                globalize(ee,t,lee)
        if((event.x)>=400 and (event.x)<500):
            if ((event.y)>=0 and (event.y)<100)and 21 in l:
                cen1=450
                cen2=50
                ee=21
                lee=[4,15,24]
                globalize(ee,t,lee)
            if ((event.y)>=100 and (event.y)<200)and 22 in l:
                cen1=450
                cen2=150
                ee=22
                lee=[4,9,16,27]
                globalize(ee,t,lee)
            if ((event.y)>=200 and (event.y)<300)and 23 in l:
                cen1=450
                cen2=250
                ee=23
                lee=[4, 9, 17]
                globalize(ee,t,lee)
            if ((event.y)>=300 and (event.y)<400)and 24 in l:
                cen1=450
                cen2=350
                ee=24
                lee=[4,9,18,22]
                globalize(ee,t,lee)
            if ((event.y)>=400 and (event.y)<500)and 25 in l:
                cen1=450
                cen2=450
                ee=25
                lee=[9,19,21]
                globalize(ee,t,lee)
        animecros(cen1,cen2)
    root.update()
    dim()
dim()
mainloop()
