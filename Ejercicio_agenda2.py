import json
import os
import sys
import re

class Agenda:
    
    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        return {}

    def validar_email(self, email):
        # Patrón básico para validar email
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None
    
    def validar_telefono(self, telefono):
        # Verifica que sea un número y tenga entre 9 y 15 dígitos
        return telefono.isdigit() and 9 <= len(telefono) <= 15
    
    def nuevo_contacto(self):
        nombre = str.title(input("Introduzca su nombre: "))
        
        # Validación de teléfono
        while True:
            telefono = input("Introduzca su número de teléfono: ")
            if self.validar_telefono(telefono):
                break
            print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 9 y 15 caracteres.")
        
        # Validación de email
        while True:
            email = input("Introduzca su email: ")
            if self.validar_email(email):
                break
            print("Email inválido. Por favor, introduzca un email válido.")
        
        # Campo adicional opcional
        direccion = input("Introduzca su dirección (opcional): ")
        
        self.contactos[nombre] = {
            "telefono": telefono,
            "email": email,
            "direccion": direccion if direccion else "No especificada"
        }
        print(f"Se ha agregado a {nombre} con el número {telefono} y con el email {email}")
    
    def buscar_contacto(self):
        print("\nBuscar contacto por:")
        print("1. Nombre")
        print("2. Teléfono")
        print("3. Email")
        opcion = input("Seleccione una opción (1-3): ")
        
        encontrados = []
        
        if opcion == "1":
            nombre = str.title(input("Introduce el nombre del contacto: "))
            if nombre in self.contactos:
                encontrados.append((nombre, self.contactos[nombre]))
        elif opcion == "2":
            telefono = input("Introduce el número de teléfono: ")
            for nombre, info in self.contactos.items():
                if info["telefono"] == telefono:
                    encontrados.append((nombre, info))
        elif opcion == "3":
            email = input("Introduce el email: ")
            for nombre, info in self.contactos.items():
                if info["email"].lower() == email.lower():
                    encontrados.append((nombre, info))
        else:
            print("Opción no válida.")
            return
        
        if encontrados:
            print("\nContactos encontrados:")
            for nombre, info in encontrados:
                print(f"\nNombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}")
                print(f"Dirección: {info['direccion']}")
        else:
            print("No se encontraron contactos con ese criterio.")

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
