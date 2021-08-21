#crearemos nuestro primer programa donde hacemos referencia a nuestra clase
class Galleta():
    chocolate=False
    pass

una_galleta=Galleta()
otra_galleta=Galleta()

print(una_galleta) ## hace referencia a la clase Galleta

# si delaro variables dentro de una clase y estas no exites automaticamente se crean 
# esta es la magia de python o por lo menos hasta se no se puede hacer en otros
# lenguajes

# por ejemplo

una_galleta.color="Naranja"
otra_galleta.sabor="Frutilla"
print(una_galleta.color)
g=Galleta()

print(g.chocolate)

class Jugo():
    bebida=False
    def __init__(self):
        print("iniciamos la clase con init")
    def servir_bedida(self):
        self.bebida=True
una_bebida=Jugo()
una_bebida.servir_bedida()
print(una_bebida.bebida)
#print(una_bebida.bebida)
## self sireve para diferenciar entre varlores de clases y metodos es 
#una regla pasarlo a cada metodo


# Ahora vamos por crear una clase llamda pelicula 
class Pelicula():
    def __init__(self,titulo=None,duracion=None,lanzamiento=None):
        if titulo is not None and duracion is not None and lanzamiento is not None:
            self.titulo=titulo
            self.duracion=duracion
            self.lanzamiento=lanzamiento
            print("se acaba de crear una nueva pelicula ","con el titulo "+titulo," con duracion "+duracion," ,y su fecha de lazamiento fue el "+lanzamiento)
        else:
            print("falta argumentos, revisar la variable pelicula")
    def __del__(self):
        print("se acaba de borrar la pelicula ", self.titulo)
pelicula=Pelicula("Titanic","1:23","10 de agosto del 1990")
del(pelicula)
#Como se puede en el ejemplo de arriba se declara como none los argumentos que se
#pasara  a la clase en caso de que se olvide enviar los argumentos desde afuera.


