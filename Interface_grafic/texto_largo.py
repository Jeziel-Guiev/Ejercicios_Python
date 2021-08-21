from tkinter import *

root=Tk()
root.title("entrada de tecto largo")

texto=Text(root)
texto.pack()
texto.config(width=30,height=20,font=("Consola",12),padx=15,pady=15)

root.mainloop()