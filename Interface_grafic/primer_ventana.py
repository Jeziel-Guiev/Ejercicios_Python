# este codigo va mostrar una ventana sencilla con tkinter
from tkinter import *
root =Tk()



root.title("mi primer ventana")
root.resizable(0,0)
root.iconbitmap("cabecera.ico")




# este loop deberia ir siempre bajo el codigo porque es el que se va ir ejecutando 
#todo el tiempo
root.mainloop()