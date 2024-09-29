#Escribe un programa que encuentre la suma de todos los números primos menores que 100.
def num_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

suma_primos = 0

for num in range(2, 100):
    if num_primo(num):
        suma_primos += num

print("La suma de todos los números primos menores que 100 es:", suma_primos)
