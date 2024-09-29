#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
#minúsculas.
def sin_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    
    for char in texto:
        if char not in vocales:
            resultado += char
            
    return resultado

cadena_usuario = input("Ingrese texto: ")
cadena_sin_vocales = sin_vocales(cadena_usuario)
print("Texto sin vocales:", cadena_sin_vocales)
