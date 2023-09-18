import random
matriz = []

while True:
    try:
        dato = input("Ingrese N: ")
        if dato != "0":
            n = int(dato)
            if n >=4 and n<=100 and n%2 !=0:
                break
    except ValueError:
        print("Eso no es un valor entero.")
lista=[]
for i in range(n):
    lista.append(random.randint(0,100))
print("la lista es: ")
print(f"{lista}\nEl resultado es:")
def Convertir(lista):
    res = int((n+1)/2)
    val = int(res/2+1)
    x=0
    y= res-1
    valor=0
    valList=0
    for i in range(res):
        fila = []
        for j in range(res):
            valor=0
            if y == j and valList< n:
                valor = lista[valList]
                valList+=1
                if y > 0:
                    y-=1
            if j==i and valList < n and j!=val-1 and i!= val-1: 
                valor=lista[valList]
                valList+=1
                x+=1 
            fila.append(valor)
        matriz.append(fila)
    return matriz
resultado = Convertir(lista)
for i in resultado:
    print(i)