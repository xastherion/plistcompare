import sys, os
from tkinter import *

mGui = Tk()


ment_01 = StringVar()
ment_02 = StringVar()
ment_03 = StringVar()

def sys_command_01():
    mtext = ment_01.get()
    os.system(mtext)
    return

def sys_command_02():
    mtext = ment_02.get()
    os.system(mtext)
    return

def sys_command_03():
    mtext = ment_03.get()
    os.system(mtext)
    return

def command_01():
   Label(mGui, text="Comando_01:").pack()
   Entry(mGui, textvariable=ment_01, width=100).pack()
   Button(mGui, text='Ejecutar', command=sys_command_01).pack()

def command_02():
   Label(mGui, text="Comando_02:").pack()
   Entry(mGui, textvariable=ment_02, width=100).pack()
   Button(mGui, text='Ejecutar', command=sys_command_02).pack()

def command_03():
   Label(mGui, text="Comando_03:").pack()
   Entry(mGui, textvariable=ment_03, width=100).pack()
   Button(mGui, text='Ejecutar', command=sys_command_03).pack()

def exit_command():
    quit()

# Principal Commands
command_01()
command_02()
command_03()

exit_button = Button(mGui, text='Exit',command=exit_command).pack(fill=X)


# -------------------------------------------------------------------
mainloop()