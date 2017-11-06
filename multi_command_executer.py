import os
from tkinter import *

mGui = Tk()

# ---------------- List of Defaults commands -----------------
lista_cmd = [
    'ls',
    'ifconfig',
    'echo "XXXXX - OOOOO - XXXXX"'
]
# ================ End Defaults Commands =====================


# ---------------- Dialog Boxes building ------------
def command_01():
    ment_01 = StringVar(mGui, value=lista_cmd[0])
    Label(mGui, text='Primer Comando')
    Entry(mGui, textvariable=ment_01, width=100).pack(fill=Y)
    Button(mGui, text='Ejecutar', command=lambda : os.system(ment_01.get())).pack(fill=Y)


def command_02():
    ment_02 = StringVar(mGui, value=lista_cmd[1])
    Entry(mGui, textvariable=ment_02, width=100).pack(fill=Y)
    Button(mGui, text='Ejecutar', command=lambda : os.system(ment_02.get())).pack(fill=Y)


def command_03():
    ment_03 = StringVar(mGui, value=lista_cmd[2])
    Entry(mGui, textvariable=ment_03, width=100).pack(fill=Y)
    Button(mGui, text='Ejecutar', command=lambda : os.system(ment_03.get())).pack(fill=Y)


# Call to DialogBox  Principal Commands
command_01()
command_02()
command_03()

# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda : quit()).pack()
# ---- End Building Exit Button --

# -------------------------------------------------------------------
mainloop()