import os
from tkinter import *

archivo = open('commands.dat', "r")

mGui = Tk()
#ment = StringVar()


while True:
    linea = archivo.readline()
    ment = StringVar(mGui, value=linea) # -- pone los comandos del archivo en el Entry
    if not linea:
        break
    Label(mGui, text="Command : ").pack()
    mentry = Entry(mGui, textvariable=ment, width=100).pack()
    Button(mGui, text='Ejecutar', command=sys_command).pack()


def exit_command():
    quit()


def sys_command():    # -- parece que no hace nada
    mtext = ment.get()
    os.system(mtext)
    return


returnButton(mGui, text='Exit',command=exit_command).grid(row=1, column=7)


archivo.closed

mainloop()