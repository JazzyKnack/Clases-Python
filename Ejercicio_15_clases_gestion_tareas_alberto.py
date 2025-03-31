# Ejercicio 15: Crea un programa que gestione una lista de tareas.
# Define una clase Tarea con atributos titulo, descripcion y completada.
# Implementa métodos para añadir, eliminar, marcar como completada y listar todas las tareas. Guarda la 
# lista de tareas en un archivo JSON y permite cargarla al iniciar el programa. Usa la librería os para 
# gestionar los archivos y directorios necesarios

import sys # Importamos el módulo sys para utilizarlo para salir del programa
import os # Importamos el módulo os para gestionar archivos y directorios
import json # Importamos el módulo json para trabajar con archivos json

class Tarea: # Creamos la clase Tarea

    def __init__(self, title = "tareas.json"): # Se inicia el constructor con el título como atributo
        # Inicializamos el archivo donde se guardarán las tares
        self.archivo = title # Ruta del archivo json
        self.tareas = self.cargar_tareas() # Cargamos las tareas desde el archivo json

    def cargar_tareas(self): # Método para cargar tareas
        if os.path.exists(self.archivo): # Si existe el archivo
            try:
                with open(self.archivo, "r") as f: # Abrir archivo en modo lectura
                    return json.load(f) # Cargamos las tareas
            except json.JSONDecodeError: # Si el archivo está vacío o tiene un formato incorrecto
                print("El archivo JSON está vacío o tiene un formato incorreto. Se inicializará una lista vacía.")
                return {} # Devuelve un diccionario vacío
        else:
            return {} # Si el archivo no existe, devuelve un diccionario vacío
        
    def guardar_tareas(self): # Método para guardar tareas
        with open(self.archivo, "w") as f: # Abrir archivo en modo escritura
            json.dump(self.tareas, f, indent=4) # Guardamos las tareas
    
    def anadir_tarea(self): # Método para añadir tarea
        try: # Método try
            titulo = input("Introduzca el nombre de la tarea: ") # Se pide al usuario que introduzca el nombre de la tarea
            if titulo == "": # Si el título está vacío
                raise ValueError("El título de la tarea no puede estar vacío.") # Mostrar mensaje de error
            descripcion = input("Introduzca la descripción de la tarea: ") # Se pide al usuario que introduzca la descripción de la tarea
            self.tareas[titulo] = {
                "Descripción": descripcion,
                "Estado": "No completada"
            } # Añadimos la tarea al diccionario de tareas
            print(f"\nLa tarea '{titulo}' ha sido añadida correctamente.") # Mostrar mensaje de tarea añadida
        except Exception as e: # Método except
            print(f"\nError al añadir la tarea: {e}") # Mostrar mensaje de error

    def eliminar_tarea(self): # Método para eliminar tarea
        try: # Método try
            titulo = input("Introduzca el nombre de la tarea que quiere borrar: ") # Se pide al usuario que introduzca el nombre de la tarea a eliminar
            if titulo in self.tareas: # Si la tarea existe en el diccionario de tareas
                del self.tareas[titulo] # Se elimina la tarea del diccionario
                print(f"\nLa tarea '{titulo}' ha sido eliminada correctamente.") # Mostrar mensaje de tarea eliminada
            else:
                raise KeyError(f"\nNo se encontró la tarea con el título '{titulo}'.") # Si la tarea no existe, se mustra mensaje de error
        except KeyError as e: # Método except con alias
            print(e) # Mostrar el error
        except Exception as e: # Método except
            print(f"\nError al eliminar la tarea: {e}") # Mostrar mensaje de error
    def marcar_completa(self): # Método para marcar la tarea como completada
        try: # Método try
            titulo = input("Introduzca el nombre de la tarea completada: ") # Se pide al usuario que introduzca el nombre de la tarea a marcar como completada
            if titulo in self.tareas: # Si la tarea existe en el diccionario de tareas
                self.tareas[titulo]["Estado"] = "Tarea completada" # Cambiamos el estado de la tarea a completada
                print(f"\nLa tarea '{titulo}' ha sido marcada como completada.") # Mostrar mensaje de tarea completada
            else:
                raise KeyError(f"\nNo se encontró la tarea con el título '{titulo}'.") # Si la tarea no existe, se muestra mensaje de error
        except KeyError as e: # Método except con alias
            print(e) # Mostrar el error
        except Exception as e: # Método except
            print(f"\nError al marcar la tarea como completada: {e}") # Mostrar mensaje de error

    def listar_tareas(self): # Método para listar todas las tareas
        if not self.tareas: # Si no hay tareas en el diccionario
            print("\nNo hay tareas en la lista.") # Mostrar mensaje de no hay tareas
        else:
            print("\nLista de tareas: ") # Mostrar mensaje de lista de tareas
            for titulo, datos in self.tareas.items(): # Recorremos el diccionario de tareas
                print(f"- {titulo}: {datos['Descripción']} [{datos['Estado']}]") # Mostramos el título, la descripción y el estado de la tarea

def menu_tareas(): # Función para el menú de opciones
    tareas = Tarea() # Creamos una instancia de la clase Tarea

    while True: # Bucle while para mostrar el menú de opciones
        print("\n*********************************")
        print("* Programa de Gestión de Tareas *")
        print("*********************************\n")
        print("Menú de opciones: ")
        print("1. Añadir tarea.") # Opción uno
        print("2. Eliminar tarea.") # Opción dos
        print("3. Marcar tarea como completada.") 
        print("4. Listar tareas.") # Opción cuatro
        print("5. Guardar y salir del programa.") 

        opcion = input("\nSeleccione una opción del 1 al 5: ") # Se pide al usuario que elija una opción

        try: # Método try
            if opcion == "1": # Si la opción es igual a uno
                tareas.anadir_tarea() # Se llama al método anadir_tarea
            elif opcion == "2": # Si la opción es igual a dos
                tareas.eliminar_tarea() 
            elif opcion == "3": # Si la opción es igual a tres
                tareas.marcar_completa() # Se llama al método marcar_completa
            elif opcion == "4": # Si la opción es igual a cuatro
                tareas.listar_tareas() # Se llama al método listar_tareas
            elif opcion == "5": # Si la opción es igual a cinco
                tareas.guardar_tareas() # Se llama al método guardar_tareas
                print("Tareas guardadas. Saliendo del programa.") # Mostrar mensaje de tareas guardadas y de salida del programa
                sys.exit() 
        except Exception as e: # Método except con alias
            print(f"Error: {e}") # Mostrar mensaje de error

if __name__ == "__main__": # Si el script se ejecuta directamente
    try: # Método try
        menu_tareas() # Se llama a la función menu_tareas
    except Exception as e: # Método except con alias
        print(f"Error en la ejecución del programa: {e}") # Mostrar mensaje de error
        sys.exit() # Salir del programa          







   



