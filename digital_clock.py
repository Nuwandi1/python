from tkinter import *
import time

def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    TimeLabel.config(text=current_time)
    window.after(1000, update_time)

window = Tk()
window.title("Digital Clock")

TimeLabel = Label(window, font=("Arial", 90))
TimeLabel.pack()

update_time()
window.mainloop()
