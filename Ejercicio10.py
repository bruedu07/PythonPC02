#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
#fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
#1636!
#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
def form_fecha(fecha):
    meses = {
        "Enero": 1,
        "Febrero": 2,
        "Marzo": 3,
        "Abril": 4,
        "Mayo": 5,
        "Junio": 6,
        "Julio": 7,
        "Agosto": 8,
        "Septiembre": 9,
        "Octubre": 10,
        "Noviembre": 11,
        "Diciembre": 12
    }
    if '/' in fecha:
        mes, dia, año = map(int, fecha.split('/'))
    elif ',' in fecha:
        mes_str, dia_str_año = fecha.split(' ')
        dia_str, año = dia_str_año.split(',')
        mes = meses[mes_str]
        dia = int(dia_str)
    else:
        raise ValueError("Formato de fecha no válido.")
    
    return f"{año}-{mes:02}-{dia:02}"

fecha_usuario = input("Ingrese una fecha (MM/DD/AAAA o 'Mes día, año'): ")
try:
    fecha_convertida = form_fecha(fecha_usuario)
    print("Fecha en formato AAAA-MM-DD:", fecha_convertida)
except ValueError as e:
    print(f"Error: {e}")

