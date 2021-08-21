resultado=0
cadena_1=input("introduzca el primer valor: ")
cadena_2=input("introduzca el segundo valor: ")
if len(cadena_1)>len(cadena_2):
    resultado=1
    print(resultado)
elif len(cadena_1)<len(cadena_2):
    resultado=2
    print(resultado)
elif len(cadena_1)==len(cadena_2):
    resultado=0
    print(resultado )