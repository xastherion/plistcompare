import sys,os
from tkinter import *

def mhello():
        mtext=ment.get()
        mlabel=Label(mGui,text=mtext).grid(row=3,column=0)
        os.system(mtext)
        return

mGui=Tk()
ment=StringVar()


mlabel=Label(mGui,text="Comando:").grid(row=0,column=0)
mentry=Entry(mGui,textvariable=ment).grid(row=0,column=1)
mbutton=Button(mGui,text='Ejecutar',command=mhello).grid(row=2,column=2)


# -------------------------------------------------------------------
mainloop()