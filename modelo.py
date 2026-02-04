import csv

def agregar_alumno(alumnos, nombre):
    alumnos.append(nombre)

def mostrar_alumno(alumnos):
    for alumno in alumnos:
        print(alumno)

def cantidad_alumno(alumnos):
    return len(alumnos)

def eliminar_alumno(alumnos, nombre):
    if nombre in alumnos:
        alumnos.remove(nombre)
        print("Alumno eliminado")
    else:
        print("No existe ese alumno")



ARCHIVO = "datos.csv"

def guardar_alumno(alumnos):
    with open(ARCHIVO, "w", newline="",encoding="utf-8") as f:
       for alumno in alumnos:
           f.write(alumno + "\n")
           
def cargar_alumno():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return [linea.strip() for linea in f]
    except FileNotFoundError:
        return []

def agregar_alumno(alumnos, nombre):
    alumnos.append(nombre)
    
def aliminar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno == nombre:
            alumnos.remove(alumno)
            break