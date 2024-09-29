#Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento.
def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
try:
    numero = int(input("Calcular el factorial de: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError as e:
    print(f"Error: {e}. Asegúrese de ingresar un número entero no negativo.")
