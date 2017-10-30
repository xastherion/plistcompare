import sys
import os
from tkinter import *
mi_comando="dir"

def ejecutar():
    os.system(nombre)
    print(mi_entrada, mi_comando, mi_boton1)

mi_gui= Tk()

nombre=StringVar()

mi_entrada=Entry(mi_gui,text=nombre)
mi_entrada.insert(END, nombre)
mi_entrada.pack()
mi_entrada.get()

mi_boton1=Button(text='OK',command=ejecutar).pack()









mi_gui.mainloop() # this is only a contruction if sometimes dont fuction