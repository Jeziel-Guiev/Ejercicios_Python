#iterar significa realizar una accion varias veces
n=0
while n<5:
    n+=1
    print(n)
else:
    print("se a completado toda la iteracion")

#break rompe el ciclo para wl while esto es muy importante
#para no entrar en un ciclo infinito

# value=0
# while value<5:
#     if value==3:
#         print("encontro el valor de 3 por lo tanto se rompe por el valor:",value)
#         break
#     value+=1
# else:
#     print("termino el ciclo while")   

# valuecontinue=0
# while valuecontinue<=5:
#     valuecontinue+=1
#     if valuecontinue==1:
#         print("encontro el valor de 3 por lo tanto se rompe por el valor:",valuecontinue)
#         continue
#     print(valuecontinue)
# else:
#     print("termino el ciclo while")    

# ccilo infinito preguntando y rompiendo


# while True:
#     print("""elige una de las tres opciones
#     1)Saludame 
#     2)Sumar dos numeros
#     3)Salir""")
#     valor=input("Elige la opcion: ")
#     if valor=="1":
#         print("Hola amigo como estas gracias por saludarme")
#     elif valor=="2":
#         data1=int(input("ingresa el primer valor entero: "))
#         data2=int(input("ingresa el segundo valor"))
#         print("la suma de los dos numeros es: ",data1+data2)
#     elif valor=="3":
#         print("gracias por utilizar nuestros servicios, hasta pronto")
#         break
#     else:
#         print("la opcion que acaba de elegir no es correcta")

while True:
    numero=int(input("introduce un numero entero multiplo de 5: "))
    if numero%5==0:
        print("el numero de acabas de ingresar es multiplo de 5 excelente, adios")
        break
    else:
        print("el numero que acabas de ingresar no es el correcto vuelve a intetarlo")