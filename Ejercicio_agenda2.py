import json # Importamos el módulo `json`
import os # Importamos el módulo `os`
import sys # Importamos el módulo `sys`
import re # Importamos el módulo `re` para trabajar con expresiones regulares

class Agenda: # Definimos la clase `Agenda`
    
    def __init__(self, archivo="contactos.json"): # Definimos el método `__init__` con un argumento opcional `archivo`
        self.archivo = archivo # Asignamos el argumento `archivo` a la variable de instancia `archivo`
        self.contactos = self.cargar_contactos() # Asignamos el resultado de la función `cargar_contactos` a la variable de instancia `contactos`

    def cargar_contactos(self): # Definimos el método `cargar_contactos`
        if os.path.exists(self.archivo): # Verificamos si el archivo existe
            with open(self.archivo, "r") as f: # Abrimos el archivo en modo lectura
                return json.load(f) # Cargamos los contactos desde el archivo
        return {} # Si el archivo no existe, devolvemos un diccionario vacío

    def validar_email(self, email): # Definimos el método `validar_email` con un argumento `email`   
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # Definimos un patrón para validar el email
        return re.match(patron, email) is not None # Verificamos si el email coincide con el patrón
    
    def validar_telefono(self, telefono): # Definimos el método `validar_telefono` con un argumento `telefono`
        return telefono.isdigit() and 9 <= len(telefono) <= 15 # Verificamos si el teléfono es un número y tiene entre 9 y 15 dígitos   
    
    def nuevo_contacto(self): # Definimos el método `nuevo_contacto`
        nombre = str.title(input("Introduzca su nombre: ")) # Solicitamos al usuario que introduzca un nombre
        
        # Validación de teléfono
        while True: # Iniciamos un bucle infinito
            telefono = input("Introduzca su número de teléfono: ") # Solicitamos al usuario que introduzca un número de teléfono
            if self.validar_telefono(telefono): # Verificamos si el teléfono es válido
                break # Salimos del bucle si el teléfono es válido
            print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 9 y 15 caracteres.") # Mensaje de error
        
        # Validación de email
        while True: # Iniciamos un bucle infinito
            email = input("Introduzca su email: ") # Solicitamos al usuario que introduzca un email
            if self.validar_email(email): # Verificamos si el email es válido
                break # Salimos del bucle si el email es válido
            print("Email inválido. Por favor, introduzca un email válido.") # Mensaje de error
        
        # Campo adicional opcional
        direccion = input("Introduzca su dirección (opcional): ") # Solicitamos al usuario que introduzca una dirección
        
        self.contactos[nombre] = { # Añadimos el contacto al diccionario `contactos`
            "telefono": telefono,
            "email": email,
            "direccion": direccion if direccion else "No especificada"
        }
        print(f"Se ha agregado a {nombre} con el número {telefono} y con el email {email}") # Mensaje de éxito
    
    def buscar_contacto(self): # Definimos el método `buscar_contacto`
        print("\nBuscar contacto por:") # Imprimimos las opciones de búsqueda
        print("1. Nombre") # Opción 1: Nombre
        print("2. Teléfono") # Opción 2: Teléfono
        print("3. Email") # Opción 3: Email
        opcion = input("Seleccione una opción (1-3): ") # Solicitamos al usuario que seleccione una opción
        
        encontrados = [] # Creamos una lista para almacenar los contactos encontrados
        
        if opcion == "1": # Si la opción es 1 (Nombre)
            nombre = str.title(input("Introduce el nombre del contacto: ")) # Solicitamos al usuario que introduzca un nombre
            if nombre in self.contactos: # Si el nombre está en el diccionario `contactos`
                encontrados.append((nombre, self.contactos[nombre])) # Añadimos el contacto a la lista de encontrados
        elif opcion == "2": # Si la opción es 2 (Teléfono)
            telefono = input("Introduce el número de teléfono: ") # Solicitamos al usuario que introduzca un número de teléfono
            for nombre, info in self.contactos.items(): # Iteramos sobre los contactos en el diccionario `contactos`
                if info["telefono"] == telefono: # Si el teléfono coincide con el teléfono del contacto
                    encontrados.append((nombre, info)) # Añadimos el contacto a la lista de encontrados
        elif opcion == "3": # Si la opción es 3 (Email)
            email = input("Introduce el email: ") # Solicitamos al usuario que introduzca un email
            for nombre, info in self.contactos.items(): # Iteramos sobre los contactos en el diccionario `contactos`   
                if info["email"].lower() == email.lower(): # Si el email coincide con el email del contacto
                    encontrados.append((nombre, info)) # Añadimos el contacto a la lista de encontrados
        else: # Si la opción no es válida
            print("Opción no válida.") # Mensaje de error
            return # Salimos del método
        
        if encontrados: # Si se encontraron contactos
            print("\nContactos encontrados:") # Imprimimos los contactos encontrados
            for nombre, info in encontrados: # Iteramos sobre los contactos encontrados
                print(f"\nNombre: {nombre}") # Imprimimos el nombre del contacto
                print(f"Teléfono: {info['telefono']}") # Imprimimos el teléfono del contacto
                print(f"Email: {info['email']}") # Imprimimos el email del contacto
                print(f"Dirección: {info['direccion']}") # Imprimimos la dirección del contacto
        else: # Si no se encontraron contactos
            print("No se encontraron contactos con ese criterio.") # Mensaje de error

    def modificar_contacto(self):
        nombre = str.title(input("Introduce el nombre del contacto a modificar: "))
        if nombre in self.contactos:
            print(f"Modificando contacto: {nombre}")
            print("Deje en blanco los campos que no desea modificar")
            
            # Teléfono
            nuevo_telefono = input(f"Nuevo teléfono ({self.contactos[nombre]['telefono']}): ")
            if nuevo_telefono:
                while not self.validar_telefono(nuevo_telefono):
                    print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 9 y 15 caracteres.")
                    nuevo_telefono = input(f"Nuevo teléfono ({self.contactos[nombre]['telefono']}): ")
                self.contactos[nombre]['telefono'] = nuevo_telefono
            
            # Email
            nuevo_email = input(f"Nuevo email ({self.contactos[nombre]['email']}): ")
            if nuevo_email:
                while not self.validar_email(nuevo_email):
                    print("Email inválido. Por favor, introduzca un email válido.")
                    nuevo_email = input(f"Nuevo email ({self.contactos[nombre]['email']}): ")
                self.contactos[nombre]['email'] = nuevo_email
            
            # Dirección
            nueva_direccion = input(f"Nueva dirección ({self.contactos[nombre]['direccion']}): ")
            if nueva_direccion:
                self.contactos[nombre]['direccion'] = nueva_direccion
            
            print(f"Contacto {nombre} modificado con éxito.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def borrar_contacto(self):
        nombre = str.title(input("Introduce el nombre del contacto a eliminar: "))
        if nombre in self.contactos:
            confirmacion = input(f"¿Está seguro de eliminar a {nombre}? (s/n): ")
            if confirmacion.lower() == 's':
                self.contactos.pop(nombre)
                print(f"Contacto {nombre} eliminado con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def guardar_agenda(self):
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent=4)
            print("Agenda guardada con éxito")
    
    def mostrar_agenda(self):
        if self.contactos:
            print("\n===== AGENDA DE CONTACTOS =====")
            for nombre, info in self.contactos.items():
                print(f"\nNombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}")
                print(f"Dirección: {info['direccion']}")
                print("-" * 30)
        else:
            print("La agenda está vacía")

def menu_agenda():
    agenda = Agenda()
    
    while True:
        print("\n********************************************")
        print("* Bienvenido a nuestra agenda de contactos *")
        print("********************************************")
        print("\nSeleccione una opción:")
        print("1. Introducir nuevo contacto")
        print("2. Modificar un contacto")
        print("3. Borrar un contacto")
        print("4. Buscar un contacto")
        print("5. Mostrar toda la agenda")
        print("6. Guardar y salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            
            if opcion == 1:
                agenda.nuevo_contacto()
            elif opcion == 2:
                agenda.modificar_contacto()
            elif opcion == 3:
                agenda.borrar_contacto()
            elif opcion == 4:
                agenda.buscar_contacto()
            elif opcion == 5:
                agenda.mostrar_agenda()
            elif opcion == 6:
                agenda.guardar_agenda()   
                print("Saliendo de la agenda")
                sys.exit()  
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    menu_agenda()
