# este codigo va mostrar una ventana sencilla con tkinter
from tkinter import *
root =Tk()
"""
root.title("mi primer ventana")
text=StringVar()
text.set("texto nuevo")
#root.resizable(0,0)
root.iconbitmap("cabecera.ico")
frame=Frame(root,width=600,height=500)
frame.config(bg="lightblue")
frame.pack()

label=Label(frame,text="hoal como estas izquierda")
label.pack(anchor="center")
label.config(bg="green",fg="blue",font=("verdana",24))
label.config(textvariable=text)
Label(root,text="estes es otro label").pack(anchor="se")
"""
imagen=PhotoImage(file="python.png")
Label(root,image=imagen,bd=0).pack()
# este loop deberia ir siempre bajo el codigo porque es el que se va ir ejecutando 
#todo el tiempo
root.mainloop()