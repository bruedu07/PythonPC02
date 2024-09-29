#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias
alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno o escriba skip: ")
    
    if nombre.lower() == 'skip':
        break
    
    notas = []
    for i in range(1, 4): 
        nota = float(input(f"Ingrese la calificación {i} (Max. 3): "))
        notas.append(nota)
    alumno = {
        'Alumno': nombre,
        'Notas': notas
    }
    
    alumnos.append(alumno)

print("\nListado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")
