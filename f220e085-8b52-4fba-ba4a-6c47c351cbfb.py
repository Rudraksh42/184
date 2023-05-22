from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime
import time
import datetime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)

style = ttk.Style(root)
style.layout("PB" ,[("Horizontal.Progressbar.trough" , 
                     {"children":[("Horizontal.Progressbar.pbar",
                     {'side':'left','sticky':'ns'})],'sticky':'nsew'}),
                     ("Horizontal.Progressbar.label",{'sticky':''})])

bar = ttk.Progressbar(root, maximum = 100, style = "PB")
bar.place(relx = 0.5 , rely= 0.1 , anchor = CENTER)
battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)

def convertT(seconds):
    Gtime = time.gmtime(seconds)
    timeR = time.strftime("%H : %M : %S" , Gtime)
    print(timeR)
    return timeR

def getBatteryLife():
    battery = psutil.sensors_battery()
    bar['value'] = battery.percent
    style.configure("PB",text = str(battery.percent) + '%')
    batteryL = convertT(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text'] = 'unplugged the battery \n rerun the code '
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKNOWN:
        battery_life['text'] = ' Did not detect battery life \m rerun the code'
    else:
        battery_life['text'] = 'battery life =' + batteryL
        root.after(1000 , getBatteryLife)
        
getBatteryLife()
root.mainloop()



