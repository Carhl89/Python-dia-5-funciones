from modelo import (
    cargar_alumnos,
    guardar_alumno,
    agregar_alumno,
    eliminar_alumno
)


alumnos = cargar_alumnos()


while True:
    print("\n--- ASISTENCIA---")
    print("1. Agregar alumno")
    print("2. Eliminar alumno")
    print("3. Listar alumno")
    print("4. Salir")
    
    opcion =input("Opcion: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        agregar_alumno(alumnos, nombre)
        guardar_alumno(alumnos)
        
    elif opcion =="2":
        nombre = input("Nombre a eliminar: ")
        eliminar_alumno(alumnos, nombre)
        guardar_alumno(alumnos)
    elif opcion == "3":
        for alumno in alumnos:
            print(alumno[0])
    elif opcion =="4":
        break
    
        