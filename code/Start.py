from Tkinter import *
import time
import os
root=Tk()
C = Canvas(width = 500, height = 500,bg="#96046d")
C.pack()
def code1():
    os.startfile("3x3.py")
    root.destroy()
def code2():
    os.startfile("5x5.py")
    root.destroy()
def choice():
    C.create_rectangle(0,0,500,500,fill="#96046d",outline="#96046d")
    a=C.create_text(250,150,text="Choose:",font=("Comic Sans MS", 30),fill="#078c5d")
    root.update
    b1=Button(root,text="3X3",font=("Comic Sans MS", 15),bg="#10a36d",fg="#720451",command=code1)
    b2=Button(root,text="5X5",font=("Comic Sans MS", 15),bg="#cc0a37",fg="#0597bf",command=code2)
    C.create_window(240,220,window=b1)
    C.create_window(240,280,window=b2)
a=C.create_text(250,220,text="Tic Tac Toe",font=("Comic Sans MS", 60),fill="#078c5d")
d=[i for i in range(50)]
for i in range(50):
    d[i]=C.create_rectangle(10*i,0,10*i+10,500,fill="#96046d",outline="#96046d")
root.update()
for i in d:
    time.sleep(0.05)
    C.delete(i)
    root.update()
    if i==d[49]:
        choice()
mainloop()
