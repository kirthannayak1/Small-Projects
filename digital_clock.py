import tkinter as tk
from time import strftime      #time , date can be used here

root= tk.Tk()
root.title("Digital Clock")

#update time and date
def time():
    string = strftime("Time: %H:%M:%S%p \nDate: %d-%m-%Y")  #format Hour,Minutes,Seconds,AM/PM, Date
    label.config(text=string)
    label.after(1000,time)   #update time after every second

label = tk.Label(root,font=('calibri',50,'bold'),background='cyan',foreground='black')
label.pack(anchor='center')      #place elements in root window
 
time()



root.mainloop()