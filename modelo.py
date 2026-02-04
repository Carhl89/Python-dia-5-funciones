import csv

def agregar_alumno(lista, nombre):
    lista.append(nombre)

def mostrar_alumno(lista):
    for alumno in lista:
        print(alumno)

def cantidad_alumnos(lista):
    return len(lista)

def eliminar_alumno(lista, nombre):
    if nombre in lista:
        lista.remove(nombre)
        print("Alumno eliminado")
    else:
        print("No existe ese alumno")



ARCHIVO = "datos.csv"

def guardar_alumno(lista):
    with open(ARCHIVO, "w", newline="",encoding="utf-8") as f:
       for alumno in lista:
           f.write(alumno + "\n")
           
def cargar_alumnos():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            return [linea.strip() for linea in f]
    
    except FileNotFoundError:
        return []

def agregar_alumno(lista, nombre):
    lista.append([nombre])
    
def aliminar_alumno(lista, nombre):
    for alumno in lista:
        if alumno[0] == nombre:
            lista.remove(alumno)
            break