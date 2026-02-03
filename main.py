import modelo

alumnos = []

modelo.agregar_alumno(alumnos, "Carlos")
modelo.agregar_alumno(alumnos, " Ana")

modelo.mostrar_alumno(alumnos)

modelo.eliminar_alumno(alumnos,"Carlos")

print("Total:",modelo.cantidad_alumnos(alumnos))