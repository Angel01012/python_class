while True:
    try:
        dato = input("Ingrese N: ")
        n = int(dato)
        break
    except ValueError:
        print("Eso no es un valor entero")
while True:
    try:
        dato = input("Ingrese M: ")
        if dato != "0" and dato != "1":
            m = int(dato)
            break
    except ValueError:
        print("Eso no es un valor entero.")
lista = []
validar = True
validar2 = False
while validar:
    lista.append(n)
    if n % m == 0:
        n =  int(n/m)
    else:
        n= n/m
    if n == 1:
        lista.append(n)
        validar =  False
        validar2=True
    else:
        if n < 1:
            validar = False
if validar2:
    for i in lista:
        print(i)
    print("es 1")
else:
    
    for i in lista:
        print(i)
    print("no es 1")
