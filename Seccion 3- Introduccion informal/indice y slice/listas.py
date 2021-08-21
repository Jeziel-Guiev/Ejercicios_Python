numeros=[1,2,3,4]
print(numeros)
lista=[1,"asdasd",353,"a"]
print(lista)
print(lista[0])
print(lista[-2:])
nuevalista=lista+[23,23,23]
nuevalista.append(11)
#print(nuevalista)
print(nuevalista)


nuevo=[2,3,4]
nuevo.append(23)
print(nuevo)

nuevo[:2]=["asd","asdasd"]
nuevo[:1]=[]
print(nuevo)
print(len(nuevo))


### listas anidadas


lista1=[2,3,2]
lista2=[23,4,3,2]
lista3=[23,23,23]

listacompleta=[lista1,lista2,lista3]
print(listacompleta)
print(listacompleta[0])
print(listacompleta[0][1])