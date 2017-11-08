import os
from tkinter import *

global new_cmd_x

mGui = Tk()

archivo = open('commands.dat', "r")


def comando():
    def new_cmd():
        #archivo.close()
        archivo = open('commands.dat', "a")
        archivo.write("\n"+ment.get())
        print(ment.get())
        return

    ment = StringVar(mGui, value=linea)
    framex = Frame(mGui)
    Button(framex, text='Save it!', command=new_cmd).pack(side=LEFT)


    Entry(framex, textvariable=ment, width=100).pack(side=LEFT)
    Button(framex, text='Do it!', command=lambda: os.system(ment.get())).pack(side=RIGHT)
    framex.pack()
    # ment.get() en Button permite que se actualice la entrada en caso de que hayan cambios en el comando


while True:             # siempre va a ser verdad por eso "break"
    linea = archivo.readline()
    if not linea:       # permite salir cuando ya no hay lineas en el archivo de comandos
        break           # sale
    comando()


# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda: quit()).pack()
# ==== End Building Exit Button ==

# ---- Building Refresh Button ------ (if something is saved)
newcmd_button = Button(mGui, text='Refresh', command=lambda: os.system("python3 test_garbage.py").pack()

# ==== End Building Exit Button ==

# -------------------------------------------------------------------
mainloop()
