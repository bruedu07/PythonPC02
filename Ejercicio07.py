#Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
#perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
#(excluyendo el propio número).
def num_perfecto(n):
    sum_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisores += i
    return sum_divisores == n

numeros_perfectos = []

for num in range(1, 1000):
    if num_perfecto(num):
        numeros_perfectos.append(num)

print("Números perfectos menores que 1000:")
print(numeros_perfectos)

