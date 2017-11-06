import sys, os
from tkinter import *
cont = 0
for schalter in range(10):

    mGui = Tk()
    ment = StringVar()


    def doit():
        mtext = ment.get()
        mlabel = Label(mGui, text="hi").pack()
        return

    def Ejecutar():
       mbutton = Button(mGui, text='Ejecutar', command=doit).pack()

    def exit_command():
        quit()

    # Principal Commands
    Ejecutar()
    cont = cont+1

    exit_button = Button(mGui, text='Exit', command=exit_command).pack()




    # -------------------------------------------------------------------
    mainloop()
