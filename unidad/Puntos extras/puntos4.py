matriz = []
matrizFinal = []
x=1
for i in range(10):
    fila = []
    fila2 = []
    for j in range(10):
        valor = x
        x+=1
        fila.append(valor)
    matriz.append(fila)
print("Matriz del 1 al 100:")
for fila in matriz:
    print(fila)
while True:
    try:
        dato = input("Ingrese N: ")
        n = int(dato)
        if n>=0 and n<11:
            break
    except ValueError:
        print("Eso no es un valor entero")
resultado=0
if n >= 0 and n <=9:
    for i in range(10):
        for j in range (10):
            if n == j:
                resultado+=matriz[i][j]
                print(matriz[i][j])
elif n == 10:
    n=0
    n2 =9
    for i in range(10):
        for j in range (10):
            if n == i:
                resultado+=matriz[i][j]
                print(matriz[i][j])
                n+=1
                resultado+=matriz[i][9-j]
                print(matriz[i][9-j])
            # if n2 == j:
            #     n2-=1
            #     resultado+=matriz[i][j]
            #     print(matriz[i][j])
print(resultado)