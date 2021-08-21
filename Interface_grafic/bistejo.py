print("hola como estas")

class Cliente():
    arrayCliente=[]
    def __init__(self):
        print('entramos a la clase')
    def guardarCliente(self,persona):
        print("guardar cliente")
        self.arrayCliente.append(persona)
        print(self.arrayCliente)

josue= Cliente()
josue.guardarCliente('josue')
#print()