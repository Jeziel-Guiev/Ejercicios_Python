matriz=[[1,2,3],[8,4,9],[5,6,7]]
#print(matriz[1][1])

# recorrer la matriz y cambiar los pares por 0 y impares por 1
#aqui todo posi
for fila,element in enumerate(matriz):
    for columna,dato in enumerate(element):
        if (matriz[fila][columna]%2==0):
            matriz[fila][columna]=0
        else:
            matriz[fila][columna]=1
print(matriz)

multiplos = []
 
# Completa el ejercicio
numero = int(input())
while numero < 0 or numero > 9:
    numero = int(input())
 
multiplos = list(range(0, 101, numero))
print(multiplos)