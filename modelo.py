import csv


def mostrar_alumno(alumnos):
    for alumno in alumnos:
        print(alumno)


def eliminar_alumno(alumnos, nombre):
    if nombre in alumnos:
        alumnos.remove(nombre)
        print("Alumno eliminado")
    else:
        print("No existe ese alumno")



ARCHIVO = "datos.csv"

def guardar_alumnos(alumnos):
    with open(ARCHIVO, "w",encoding="utf-8") as f:
       for nombre, estado in alumnos:
           f.write(f"{nombre},{estado}\n")
           
def cargar_alumnos():
    alumnos = []
    
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            nombre, estado = linea.split(",")
            alumnos.append([nombre, estado])
        return alumnos

def agregar_alumno(alumnos, nombre):
    alumnos.append([nombre, "A"])
    return alumnos
    
def eliminar_alumno(alumnos, nombre):
    for alumno in alumnos:
        if alumno[0] == nombre:
            alumnos.remove(alumno)
            break
    return alumnos

def marcar_asistencia(lista, nombre, estado):
    for alumno in lista:
        if alumno[0] == nombre:
            alumno[1] = estado
            break