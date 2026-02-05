from modelo import *


alumnos = cargar_alumnos()


while True:
    print("\n--- ASISTENCIA---")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Listar alumno")
    print("4. Marcar presente")
    print("5. Marcar ausente")
    print("6. Salir")
    
    opcion =input("Opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        alumnos = agregar_alumno(alumnos, nombre)
        guardar_alumnos(alumnos)
        
    elif opcion =="2":
        nombre = input("Nombre a eliminar: ")
        alumnos = eliminar_alumno(alumnos, nombre)
        guardar_alumnos(alumnos)
        
    elif opcion == "3":
        for nombre, estado in alumnos:
            estado_txt ="Presente" if estado == "P" else "Ausente"
            print(nombre, "-", estado_txt)
            
            
    elif opcion =="4":
        nombre = input("Nombre: ")
        marcar_asistencia(alumnos, nombre, "P")
        guardar_alumnos(alumnos)
    
    elif opcion == "5":
        nombre = input("Nombre: ")
        marcar_asistencia(alumnos, nombre, "A")
        guardar_alumnos(alumnos)
    
    elif opcion == "6":
        break