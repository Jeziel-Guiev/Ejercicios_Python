# dada dos listas realizar los siguientes ejercicios 

lista1=[1,12,123]
lista2=["Bye","Ciao","Ägur","Adieu"]


lista1.append(1234)
lista1.append("Hola")
#lista1+[1234,"Ho"]
print(lista1)

lista2.append("Adios")
lista2.append(1234)
print(lista2)

lista1[-1:]=[] # este verificar y ver la solucion final
lista3=lista1
print(lista3)


lista2[:1]=[]
lista2[-1:]=[]
lista4=lista2
print(lista4)

lista5=lista3+lista4
print(lista5)

