import os
from tkinter import *

mGui = Tk()

# ---------------- List of Defaults commands -----------------
lista_cmd = [
    'ls',
    'ifconfig',
    'echo "XXXXX - OOOOO - XXXXX"',
    '',
    ''
]

lista_elem = (len(lista_cmd)) # --> cuenta los elementos en la lista_cmd
# ================ End Defaults Commands =====================

# ---------------- Dialog Boxes building ------------
def command_01():
    ment_01 = StringVar(mGui, value=lista_cmd[0])
    frame_01 = Frame(mGui)
    Entry(frame_01, textvariable=ment_01, width=100).pack(side=LEFT)
    Button(frame_01, text='Ejecutar', command=lambda: os.system(ment_01.get())).pack(side=RIGHT)
    frame_01.pack()


def command_02():
    ment_02 = StringVar(mGui, value=lista_cmd[1])
    frame_02 = Frame(mGui)
    Entry(frame_02, textvariable=ment_02, width=100).pack(side=LEFT)
    Button(frame_02, text='Ejecutar', command=lambda: os.system(ment_02.get())).pack(side=RIGHT)
    frame_02.pack()


def command_03():
    ment_03 = StringVar(mGui, value=lista_cmd[2])
    frame_03 = Frame(mGui)
    Entry(frame_03, textvariable=ment_03, width=100).pack(side=LEFT)
    Button(frame_03, text='Ejecutar', command=lambda: os.system(ment_03.get())).pack(side=RIGHT)
    frame_03.pack()
# ================ End Dialog Boxes building ==================


# Call to Dialog Boxes Principal Commands
command_01()
command_02()
command_03()

# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=lambda : quit()).pack()
# ==== End Building Exit Button ==


# -------------------------------------------------------------------
mainloop()