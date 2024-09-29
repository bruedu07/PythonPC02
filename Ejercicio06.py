#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números:
#0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.

fibonacci = [0, 1]

while True:
    numero_sig = fibonacci[-1] + fibonacci[-2]
    if numero_sig > 50:
        break
    fibonacci.append(numero_sig)

print("Serie de Fibonacci entre 0 y 50:")
print(fibonacci)

