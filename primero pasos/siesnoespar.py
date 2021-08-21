final=int(input("ingresa un valor decimal entero menor a 100: "))
n=0
while n<=final:
    if(n%2==0):
        print("es numero par " +str(n))
    else:
        print("es numero impar "+str(n))
    n=n+1