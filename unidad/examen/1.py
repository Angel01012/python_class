import random
matriz = []
lista=[]
filaAux = []
while True:
    try:
        dato = input("Ingrese N: ")
        if dato != "0":
            n = int(dato)
            if n >=2 and n<=10:
                break
    except ValueError:
        print("Eso no es un valor entero.")
def LLenado (n):
    for i in range(n):
        fila = []
        for j in range(n):
            valor = random.randint(1,100)
            fila.append(valor)
            filaAux.append(valor)
        matriz.append(fila)
    return matriz
m = LLenado(n)
for i in m:
    print(i)
print("lista ordenada")
matrizFinal=[]
ordenados = sorted(filaAux)
x=0
for i in range(n):
    listFinal=[]
    for j in range(n):
        listFinal.append(ordenados[x])
        x+=1
    matrizFinal.append(listFinal)
for i in matrizFinal:
    print(i)