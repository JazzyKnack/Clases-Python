import json # Importamos la librería json para trabajar con archivos JSON 
import os # Importamos la librería os para trabajar con el sistema operativo
import sys # Importamos la librería sys para trabajar con el sistema

class Agenda: # Creamos la clase Agenda
    
    def __init__(self, archivo="contactos.json"): # Definimos el método __init__ con un argumento opcional
        self.archivo = archivo # Asignamos el argumento "archivo" a la variable de instancia "archivo"
        self.contactos =  self.cargar_contactos() # Asignamos el resultado de la función "cargar_contactos" a la variable de instancia "contactos"

    def cargar_contactos(self): # Definimos el método "cargar_contactos"
        try: # Iniciamos un bloque "try"
            if os.path.exists(self.archivo):  # método de os para saber si esxiste el archivo
                with open(self.archivo, "r") as f:   # abrir el archivo
                    return json.load(f)              # y lo carga
            return {} # Si no existe el archivo, devuelve un diccionario vacío
        except json.JSONDecodeError: # Excepción para errores de decodificación JSON
            print("Error: El archivo JSON está coprrupto.") # Mensaje de error
            return{} # Devuelve un diccionario vacío
        except FileNotFoundError: # Excepción para archivos no encontrados
            print("Archivo no encontrado, creando uno nuevo") # Mensaje de error
            return{} # Devuelve un diccionario vacío
        except Exception as e: # Excepción genérica
            print(f"Error al cargar contacto {e}") # Mensaje de error
            return{} # Devuelve un diccionario vacío
    
    def nuevo_contacto(self): # Definimos el método `nuevo_contacto`
        try: # Iniciamos un bloque "try"
            nombre = str.title(input("Introduzca su nombre: ")) # Solicitamos al usuario que introduzca un nombre
            telefono = int(input("Introduzca su número de teléfono: ")) # Solicitamos al usuario que introduzca un número de teléfono
            email = input("Introduzca su email: ") # Solicitamos al usuario que introduzca un email
            self.contactos [nombre] = { "telefono" : telefono, "email" : email} # Añadimos el contacto al diccionario "contactos"
            print(f"Se ha agregado a {nombre} con el número {telefono} y con el email {email}") # Mensaje de éxito
        except ValueError: # Excepción para errores de valor
            print("Error: El número de teléfono debe ser un número entero") # Mensaje de error
        except KeyError:
            print("Error: El contacto ya existe") # Mensaje de error
        except ValueError:
            print("Error: El nombre debe ser una cadena de texto") # Mensaje de error
        except ValueError:
            print("Error: El email debe ser una cadena de texto") # Mensaje de error
        
    
    def buscar_contacto(self): # Definimos el método "buscar_contacto"
        try: # Iniciamos un bloque "try"
            nombre = str.title(input("Introduce el nombre del contacto a buscar: ")) # Solicitamos al usuario que introduzca un nombre
            if nombre in self.contactos: # Si el nombre está en el diccionario "contactos" 
                info = self.contactos[nombre] # Asignamos la información del contacto a la variable "info"
                print(f"Nombre: {nombre}") # Imprimimos el nombre del contacto
                print(f"Teléfono: {info['telefono']}") # Imprimimos el teléfono del contacto
                print(f"Email: {info['email']}") # Imprimimos el email del contacto
            else: # Si el nombre no está en el diccionario "contactos"
                print(f"Contacto {nombre} no encontrado.") # Mensaje de error
        except Exception as e: # Excepción genérica
            print(f"Error al buscar contacto {e}") # Mensaje de error
        except ValueError: # Excepción para errores de valor
            print("Error: El nombre debe ser una cadena de texto") # Mensaje de error
        except KeyError: # Excepción para errores de clave
            print("Error: El contacto no existe") # Mensaje de error

    def borrar_contacto(self): # Definimos el método "borrar_contacto"
        try: # Iniciamos un bloque "try"
            nombre = str.title(input("Introduce el nombre del contacto a eliminar: ")) # Solicitamos al usuario que introduzca un nombre
            if nombre in self.contactos: # Si el nombre está en el diccionario "contactos"
                self.contactos.pop(nombre) # Eliminamos el contacto del diccionario "contactos"
                print(f"Contacto {nombre} eliminado con éxito.") # Mensaje de éxito
            else: # Si el nombre no está en el diccionario "contactos"
                print(f"Contacto {nombre} no encontrado.") # Mensaje de error
        except Exception as e: # Excepción genérica
            print(f"Error al eliminar contacto {e}") # Mensaje de error
        except ValueError: # Excepción para errores de valor
            print("Error: El nombre debe ser una cadena de texto") # Mensaje de error
        except KeyError: # Excepción para errores de clave
            print("Error: El contacto no existe") # Mensaje de error        

    def guardar_agenda(self): # Definimos el método "guardar_agenda"
        try: # Iniciamos un bloque "try"
            with open(self.archivo, "w") as f: # Abrimos el archivo en modo escritura
                json.dump(self.contactos, f, indent = 4) # Guardamos el diccionario "contactos" en el archivo  
                print("Agenda guardada con éxito") # Mensaje de éxito
        except PermissionError: # Excepción para errores de permisos
            print("Error. No hay permisos para excribir en el archivo") # Mensaje de error
        except Exception as e: # Excepción genérica
            print(f"Error al guardar la agenda {e}") # Mensaje de error
    
    def mostrar_agenda(self): # Definimos el método "mostrar_agenda"
        try: # Iniciamos un bloque "try"
            if self.contactos:   # Si se pone is True o == True sale que la agenda está vacía.
                for nombre, info in self.contactos.items():    # Si le damos solo nombre recorre las claves y si le damos info también recorre los valores
                    print(f"\nNombre: {nombre}") # Imprimimos el nombre del contacto
                    print(f"Teléfono: {info['telefono']}") # Imprimimos el teléfono del contacto
                    print(f"Email: {info['email']}\n") # Imprimimos el email del contacto
            else: # Si la agenda está vacía
                print("La agenda está vacía") # Mensaje de error
        except Exception as e: # Excepción genérica
            print(f"Error al mostrar agenda {e}") # Mensaje de error

def menu_agenda(): # Definimos la función "menu_agenda"
    while True: # Iniciamos un bucle infinito
        print("\n********************************************")
        print("* Bienvenido a nuestra agenda de contactos *") # Menú de la agenda
        print("********************************************")
        print("\nSeleccione una opción:") # Menú de opciones    
        print("1. Introducir nuevo contacto") # Opción 1
        print("2. Borrar un contacto") # Opción 2   
        print("3. Buscar un contacto") # Opción 3
        print("4. Mostrar toda la agenda") # Opción 4
        print("5. Salir") # Opción 5
        opcion = int(input("Selecciona una opción: ")) # Solicitamos al usuario que seleccione una opción

        if opcion == 1: # Si el usuario selecciona la opción 1  
            agenda_test.nuevo_contacto() # Llamamos al método "nuevo_contacto"  
        elif opcion == 2: # Si el usuario selecciona la opción 2
            agenda_test.borrar_contacto() # Llamamos al método "borrar_contacto"
        elif opcion == 3: # Si el usuario selecciona la opción 3
            agenda_test.buscar_contacto() # Llamamos al método "buscar_contacto"
        elif opcion == 4: # Si el usuario selecciona la opción  4
            agenda_test.mostrar_agenda() # Llamamos al método "mostrar_agenda"
        elif opcion == 5: # Si el usuario selecciona la opción 5
            agenda_test.guardar_agenda() # Llamamos al método "guardar_agenda"  
            print("Saliendo de la agenda") # Mensaje de salida
            sys.exit() # Salimos del programa 
        else: # Si el usuario selecciona una opción no válida
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.") # Mensaje de error


agenda_test = Agenda() # Creamos una instancia de la clase "Agenda"
menu_agenda() # Llamamos a la función "menu_agenda"

if __name__ == "__main__": # Si el script se ejecuta directamente
    try: # Iniciamos un bloque "try"
        menu_agenda() # Llamamos a la función "menu_agenda"
    except Exception as e: # Excepción genérica
        print(f"Error en la ejecución del programa: {e}") # Mensaje de error
        sys.exit() # Salimos del programa   

