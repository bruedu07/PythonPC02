#Escriba un programa en Python para construir el siguiente patrón.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

lineas = 5

for i in range(1, lineas + 1):
    print('* ' * i)

# Parte inferior del patrón
for i in range(lineas - 1, 0, -1):
    print('* ' * i)
