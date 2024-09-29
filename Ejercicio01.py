#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).
R_inferior = 1500
R_Superior = 2700
resultados = []

for num in range(R_inferior, R_Superior + 1):
    if num % 7 == 0 and num % 5 == 0:
        resultados.append(num)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(resultados)
