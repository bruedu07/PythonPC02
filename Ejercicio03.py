#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.

numeros = []

while True:
    respuesta = input("¿Desea ingresar un número?: ").strip().upper()
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Debe contestar SI o NO")

pares = 0
impares = 0

for datos in numeros:
    if datos % 2 == 0:
        pares += 1
    else:
        impares += 1

# Resultados
print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

