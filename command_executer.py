import sys, os
from tkinter import *

mGui = Tk()
ment = StringVar()

def sys_command():
    mtext = ment.get()
    mlabel = Label(mGui, text=mtext).grid(row=3, column=0)
    os.system(mtext)
    return

def one_command():
   mlabel = Label(mGui, text="Comando:").grid(row=0, column=0)
   mentry = Entry(mGui, textvariable=ment, width=100).grid(row=0, column=1)
   mbutton = Button(mGui, text='Ejecutar', command=sys_command).grid(row=0, column=7)

def exit_command():
    quit()

# Principal Commands
one_command()

exit_button = Button(mGui, text='Exit',command=exit_command).grid(row=1, column=7)


# -------------------------------------------------------------------
mainloop()