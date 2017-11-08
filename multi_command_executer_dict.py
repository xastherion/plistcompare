# Python script for diferents configurations commands.
# Usage: Easy put your commands in the dictionary "lista_cmd"
# with a number. So you have your commands colection. If you need one
# one of these commands, you need only press the button "Do it!"
# if you need to edit some command for little variations and you dont
# whant to save this variations, you can edit the command in the entry
# and then, press "Do it!" for this command

import os
from tkinter import *

mGui = Tk()

# ---------------- List of Defaults commands ----------------------
lista_cmd = {
    0:'ls',
    1:'ifconfig',
    2:'echo "XXXXX - OOOOO - XXXXX"',
    3:'',
    4:'',
    5:'hey'
}
# ================ End Defaults Commands ===========================

# ---------------- Dialog Boxes building ---------------------------
for cont in lista_cmd:
    print(cont)
    def command_01():
        leer_lista = StringVar(mGui, value=lista_cmd[cont])
        framex = Frame(mGui)
        Entry(framex, textvariable=leer_lista, width=100).pack(side=LEFT)
        Button(framex, text='Do it!', command=lambda: os.system(leer_lista.get())).pack(side=RIGHT)
        framex.pack()

    command_01()
# ================ End Dialog Boxes building =======================




# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda : quit()).pack()
# ==== End Building Exit Button ==

# -------------------------------------------------------------------
mainloop()