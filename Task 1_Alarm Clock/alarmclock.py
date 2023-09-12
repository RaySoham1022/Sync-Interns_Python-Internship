from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print("Current Time : ", end="")
        print(now)
        if now == set_alarm:
            print("Alarm Ringing.......")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

clock = Tk()
clock.title("Sync Intern Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= " Use 24 Hour Format ", fg="red",font="Arial").place(x=90,y=120)
names=Label(clock, text= "(Made by Soham Ray)", fg="green",font=('Helevetica',10,'bold')).place(x=120,y=170)
addTime = Label(clock,text = "Hour   Min    Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Set Alarm Time :",fg="blue",font=('Helevetica',7,'bold')).place(x=20, y=29)

#set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 15).place(x=200,y=30)

#input by user:
submit = Button(clock,text = "Set",fg="red",bg="white",width = 10,command = actual_time).place(x =150,y=70)

clock.mainloop()