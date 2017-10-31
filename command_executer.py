import sys, os
from tkinter import *

mGui = Tk()
ment = StringVar()

def mhello():
    mtext = ment.get()
    mlabel = Label(mGui, text=mtext).grid(row=3, column=0)
    os.system(mtext)
    return

def one_command():
   mlabel = Label(mGui, text="Comando:").grid(row=0, column=0)
   mentry = Entry(mGui, textvariable=ment, width=100).grid(row=0, column=1)
   mbutton = Button(mGui, text='Ejecutar', command=mhello).grid(row=0, column=7)

def exit_command():
    quit()

# Principal Commands
one_command()
one_command()

add_button = Button(mGui, text='Add Comando',command=one_command()).grid(row=1, column=1)
exit_button = Button(mGui, text='Exit',command=exit_command).grid(row=1, column=7)

grid_label='grid(row=0, column=0)'
grid_entry='grid(row=0, column=1)'
grid_button='grid(row=0, column=7)'
position=(grid_label, grid_entry, grid_button)


# -------------------------------------------------------------------
mainloop()