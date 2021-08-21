# este codigo va mostrar una ventana sencilla con tkinter
from tkinter import *
root =Tk()



root.title("mi primer ventana")
#root.resizable(0,0)
root.iconbitmap("cabecera.ico")

frame=Frame(root)
# frame.pack(side="bottom",anchor="e")
frame.pack(fill="both",expand=1)
frame.config(width=600,height=500)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="black")
root.config(bd=25)
root.config(relief="ridge")


# este loop deberia ir siempre bajo el codigo porque es el que se va ir ejecutando 
#todo el tiempo
root.mainloop()