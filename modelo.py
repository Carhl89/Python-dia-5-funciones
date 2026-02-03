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