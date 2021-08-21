##  vamos a imprimir los valores de una lista
lista=[1,2,3,4,5,6,7,8,9,10]
for element in lista:
    print(element)

#ahora para poder obtener el indice de cada iteracion 
#se puede utilizar enumerate[lista]

numeros=[1,2,3,4,5,6,7,8,9,10]
for index,element in enumerate(numeros):
    numeros[index]*=10
print(numeros)

cadena="hola amigos como estan"
for letter in cadena:
    print(letter)