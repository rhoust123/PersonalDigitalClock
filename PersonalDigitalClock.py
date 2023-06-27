# Personal Coding Project
# Author: Rhett Houston
# Start Date: 6/26/23
# End Date: //23
# Sources: Johan Godinho (Python Tutorial - How to create a digital clock using python and tkinter - for beginners)
# Sources cont'd: https://www.youtube.com/watch?v=3FpqXyJsd1s


import time
import sys
from tkinter import Tk
from tkinter import Label


# define master screen
master = Tk()
master.title("Digital Clock")


def get_the_time():
    timex = time.strftime("%I:%M:%S %p")

    # add text to clock label
    clock.configure(text=timex)
    # clock.after(1000, get_the_time())


# create clock label
clock = Label(master, font=("Calibri", 90), bg="white", fg="black")
clock.configure(text="HEY")

# pack places label on center of screen
clock.place(x=70,y=70)

# get_the_time()

master.mainloop()
