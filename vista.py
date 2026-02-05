import tkinter as tk
from tkinter import messagebox
from modelo import *

alumnos = cargar_alumnos()

#=========================

# FUNCIONES DE BOTONES

#=========================


def agregar():
    nombre = entry_nombre.get()
    
    if not nombre:
        return
    global alumnos
    alumnos = agregar_alumno(alumnos, nombre)
    guardar_alumnos(alumnos)
    actualizar_lista()
    entry_nombre.delete(0, tk.END)
    
def eliminar():
    nombre = entry_nombre.get()
    
    global alumnos
    alumnos = eliminar_alumno(alumnos, nombre)
    guardar_alumnos(alumnos)
    actualizar_lista()
    entry_nombre.delete(0,tk.END)
    
def presente():
    nombre = entry_nombre.get()
    marcar_asistencia(alumnos, nombre, "P")
    guardar_alumnos(alumnos)
    actualizar_lista()
    
def ausente():
    nombre = entry_nombre.get()
    marcar_asistencia(alumnos, nombre, "A")
    guardar_alumnos(alumnos)
    actualizar_lista()
    
def actualizar_lista():
    lista.delete(0, tk. END)
    
    for nombre, estado in alumnos:
        estado_txt = "Presente" if estado == "P" else "Ausente"
        lista.insert(tk.END, f"{nombre}-{estado_txt}")

#====================
# VENTANA
#====================

ventana = tk.Tk()
ventana.title("App de Asistencia")
ventana.configure(bg="#2C3E50")
ventana.geometry("400x400")

#Entrada nombre

entry_nombre = tk.Entry(ventana, width=30, bg= "#ecf0f1", fg= "black", font=("Arial", 12))
entry_nombre.pack(pady=10)

# Botones
tk.Button(ventana, text="Agragar", command=agregar, bg= "#27AE60").pack(pady=3)
tk.Button(ventana, text= "Eliminar", command=eliminar, bg= "#E74C3C").pack(pady=3)
tk.Button(ventana, text="Marcar presente", command=presente, bg= "#3998db").pack(pady=3)
tk.Button(ventana, text= "Marcar asusente", command=ausente, bg= "#f39c12").pack(pady=3)

# Lista de alumnos

lista = tk.Listbox(ventana, width=40, bg="white", fg= "black", font=("Arial", 11))
lista.pack(pady=15)

actualizar_lista()
ventana.mainloop()