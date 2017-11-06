import os
from tkinter import *

mGui = Tk()

# ---------------- List of Defaults commands -----------------
lista_cmd = [
    'ls',
    'ifconfig',
    'echo "XXXXX - OOOOO - XXXXX"'
]
# ---------------- End Defaults Commands -------------


ment_01 = StringVar(mGui, value=lista_cmd[0])
ment_02 = StringVar(mGui, value=lista_cmd[1])
ment_03 = StringVar(mGui, value=lista_cmd[2])


# ----- Execution in System --------------
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

# ------ End Execution in System ----------

# ------ Dialog Boxes building ------------

def command_01():
    Label(mGui, text="Comando_01:").pack()
    Entry(mGui, textvariable=ment_01, width=100).pack()
    Button(mGui, text='Ejecutar', command=sys_command_01).pack()


def command_02():
    Label(mGui, text="Comando_02:").pack()
    Entry(mGui, textvariable=ment_02, width=100).pack()
    Button(mGui, text='Ejecutar', command=sys_command_02).pack()


def command_03():
    Label(mGui, bg='blue', text="Comando_03:").pack()
    Entry(mGui, textvariable=ment_03, width=100).pack()
    Button(mGui, text='Ejecutar', command=sys_command_03).pack()


# --- Button Exit ------
def exit_command():
    quit()
# --- End Exit Button --


# Principal Commands
command_01()
command_02()
command_03()
print(lista_cmd[0])

# ---- Building Exit Button ------
exit_button = Button(mGui, text='Exit', command=exit_command).pack()
# ---- End Building Exit Button --


<<<<<<< HEAD
# -------------------------------------------------------------------
=======
# --------------------------------------------------------------------
>>>>>>> origin/master
mainloop()
