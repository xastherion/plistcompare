from tkinter import *
doit=1
main_window = Tk()
exit_button = Button(main_window, text='exit').pack()

while exit_button!=0:
    def Ejecutar():
        mbutton = Button(main_window, text='Ejecutar').pack()
        main_label = Label(main_window, text="Hello").pack()
    Ejecutar()


# -----------------------------
mainloop()