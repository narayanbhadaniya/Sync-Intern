from tkinter import *
import datetime
import time
import winsound
from PIL import Image, ImageTk

window=Tk()
window.title("Alark Clock")
window.config(bg="Skyblue")

rw=550
rh=430
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(rw/2)
hpos=(sh/2)-(rh/2)
window.geometry("%dx%d+%d+%d"%(rw,rh,wpos,hpos))
window.maxsize(2560,1600)
window.minsize(650,450)

 
def Alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        actual_time = datetime.datetime.now()
        cur_time = actual_time.strftime("%H:%M:%S")
        cur_date = actual_time.strftime("%d/%m/%Y")
        msg="Current Time: "+str(cur_time)
        print(msg)
        if cur_time == set_alarm_timer:
            winsound.PlaySound("Music.wav",winsound.SND_ASYNC)
            print("Beep Beep Beep..........Wake Up")
            break
 
def get_alarm_time():
    alarm_set_time = f"{hour.get()}:{min.get()}:{sec.get()}"
    Alarm(alarm_set_time)

#head label
h=Label(window,text="24 Hour Alarm Clock",width=0,height=0,font=("comic sans ms",15,"bold underline"))
h.config(bg="white",fg="Black")
h.place(x=220,y=20)

alarm=ImageTk.PhotoImage(file="Images\\alarm.png")
add=Label(image=alarm)
add.place(x=250,y=70)


addTime = Label(window,text = "Hour    Min    Sec",font=60,fg="white",bg="black").place(x=310,y=220)
setYourAlarm = Label(window,text = "Set Time for Alarm: ",fg="white",bg="#922B21",relief = "solid",font=("Helevetica",15,"bold")).place(x=100, y=235)
 
hour = StringVar()
min = StringVar()
sec = StringVar()
 
hourTime= Entry(window,textvariable = hour,bg = "#48C9B0",width = 4,font=(20)).place(x=310,y=250)
minTime= Entry(window,textvariable = min,bg = "#48C9B0",width = 4,font=(20)).place(x=370,y=250)
secTime = Entry(window,textvariable = sec,bg = "#48C9B0",width = 4,font=(20)).place(x=430,y=250)
 
submit = Button(window,text = "Set Your Alarm",fg="Black",bg="#D4AC0D",width = 15,command = get_alarm_time,font=(20)).place(x =230,y=290)

 #head label
h=Label(window,text="Developed By Narayan Bhadaniya ⏰",width=0,height=0,font=("comic sans ms",20,"bold"))
h.config(bg="skyblue",fg="Black")
h.place(x=100,y=400)
window.mainloop()
