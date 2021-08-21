from tkinter import *
root=Tk()
root.title("entradas")



label = Label(root, text="Nombre muy largo")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="?")

# Finalmente bucle de la aplicación
root.mainloop()

# frame=Frame(root)
# frame.pack()
# entrada=Entry(frame)
# entrada.pack(side="right")
# label1=Label(frame,text="ingresar informacion")
# label1.pack(side="left")
# frame2=Frame(root)
# frame2.pack()
# entrada2=Entry(frame2)
# entrada2.pack(side="right")
# label2=Label(frame2,text="Apellidos      ")
# label2.pack(side="left")

