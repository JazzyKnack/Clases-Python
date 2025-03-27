# Ejercicio 15: Crea un programa que gestione una lista de tareas.
# Define una clase Tarea con atributos titulo, descripcion y completada.
# Implementa métodos para añadir, eliminar, marcar como completada y listar todas las tareas. Guarda la 
# lista de tareas en un archivo JSON y permite cargarla al iniciar el programa. Usa la librería os para 
# gestionar los archivos y directorios necesarios


import os # Importamos librería os
import json # Importamos librería json

class Tarea: # Creamos la clase Tarea

    def __init__(self, title = "recursos/tareas.json"): # Se inicia el constructor con el título como atributo
        self.archivo = title # Para poder cargar varias agendas
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self): # Método para cargar tareas
        if os.path.exists(self.archivo): # Si existe el archivo
            with open(self.archivo, "r") as f: # Que lo abra
                return json.loads(f) # Y lo cargue
        else:
            return {} # Devuelve un diccionario vacío
        
    def anadir_tarea(self): # Método para añadir tarea
        self.titulo = input("Introduzca el nombre de la tarea: ") # Se pide al usuario que introduzca el nombre de la tarea
        self.descripcion = input("Introduzca la descripción de la tarea: ") # Se pide al usuario que introduzca la descripción de la tarea
        self.completada = "No completada"
        self.tareas[self.titulo] = {
            "Descripción" : self.descripcion,
            "Estado" : self.completada
        }

    def eliminar_tarea(self):
        self.delete = input("Introduzca la tarea que quiere borrar: ")
        self.tareas.pop(self.delete)


tarea = Tarea()

