import os
from tkinter import *

mGui = Tk()

archivo = open('commands.dat', "r")

def new_cmd():
    archivo = open('commands.dat', "w")

while True:             # siempre va a ser verdad por eso "break"
    linea = archivo.readline()
    if not linea:       # permite salir cuando ya no hay lineas en el archivo de comandos
        break           # sale

    def comando():
        ment = StringVar(mGui, value=linea)
        framex = Frame(mGui)
        Button(framex, text='Save it!', command=lambda: os.system(ment.get())).pack(side=LEFT)
        Entry(framex, textvariable=ment, width=100).pack(side=LEFT)
        Button(framex, text='Do it!', command=lambda: os.system(ment.get())).pack(side=RIGHT)
        framex.pack()

# ment.get() permite que se actualice la entrada en caso de que hayan cambios en el comando

    comando()

# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda: quit()).pack()
# ==== End Building Exit Button ==
# ---- Building Exit Button ------
newcmd_button = Button(mGui, text='Refresh', command=lambda: quit()).pack()
# ==== End Building Exit Button ==

# -------------------------------------------------------------------
mainloop()
