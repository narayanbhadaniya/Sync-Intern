import pyshorteners
from tkinter import *

window=Tk()
window.title("URL Shortner")
window.config(bg="White")

rw=550
rh=430
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
window.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
window.maxsize(2560,1600)
window.minsize(650,450)

def short():
    global s_url
    url = e1.get()
    short = pyshorteners.Shortener()
    s_url = short.tinyurl.short(url)
    L2.config(text=s_url)

def copy_select():
    global data 
    data=s_url.selection_get()

 #head label
h=Label(window,text="URL Shortner With Python",width=0,height=0,font=("comic sans ms",25,"bold"))
h.config(bg="white",fg="Red")
h.place(x=120,y=20)

#mail
l1=Label(window,text="Enter Your URl Link:",width=0,height=0,font=("Comic Sans MS",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=190,y=100)
e1=Entry(window,font=(6))
e1.configure(bg="white",fg="Black")
e1.place(x=220,y=170)
b1=Button(window,text="Ok",width=10,height=0,font=("Comic Sans MS",17,"bold"),command=short)
b1.config(bg="white",fg="Red")
b1.place(x=250,y=230)



l1=Label(window,text="Short Link is:",width=0,height=0,font=("Comic Sans MS",20,"bold"))
l1.configure(bg="white",fg="black")
l1.place(x=240,y=300)
L2=Label(window,text="",width=30,height=0,font=("Comic Sans MS",15,"bold"))
L2.configure(bg="Skyblue",fg="Black")
L2.place(x=155,y=350)
b2=Button(window,text="Copy Link",width=10,height=0,font=("Comic Sans MS",12,"bold"))
b2.config(bg="white",fg="Green")
b2.place(x=270,y=400)



window.mainloop()

