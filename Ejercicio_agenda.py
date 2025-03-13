import json
import os
import sys

class Agenda:
    
    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos =  self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo):  # método de os para saber si esxiste el archivo
            with open(self.archivo, "r") as f:   # abrir el archivo
                return json.load(f)              # y lo carga
        return {}

    def nuevo_contacto(self):
        nombre = str.title(input("Introduzca su nombre: "))
        telefono = int(input("Introduzca su número de teléfono: "))
        email = input("Introduzca su email: ")
        self.contactos [nombre] = { "telefono" : telefono, "email" : email}
        print(f"Se ha agregado a {nombre} con el número {telefono} y con el email {email}")
    
    def buscar_contacto(self):
        nombre = str.title(input("Introduce el nombre del contacto a buscar: "))
        if nombre in self.contactos:
            info = self.contactos[nombre]
            print(f"Nombre: {nombre}") 
            print(f"Teléfono: {info['telefono']}") 
            print(f"Email: {info['email']}")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def borrar_contacto(self):
        nombre = str.title(input("Introduce el nombre del contacto a eliminar: "))
        if nombre in self.contactos:
            self.contactos.pop(nombre)
            print(f"Contacto {nombre} eliminado con éxito.")
        else:
            print(f"Contacto {nombre} no encontrado.")

    def guardar_agenda(self):
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent = 4)
            print("Agenda guardada con éxito")
    
    def mostrar_agenda(self):
        if self.contactos:   # Si se pone is True o == True sale que la agenda está vacía.
            for nombre, info in self.contactos.items():    # Si le damos solo nombre recorre las claves y si le damos info también recorre los valores
                print(f"\nNombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        else:
            print("La agenda está vacía")

def menu_agenda():
    while True:
        print("\n********************************************")
        print("* Bienvenido a nuestra agenda de contactos *")
        print("********************************************")
        print("\nSeleccione una opción:")
        print("1. Introducir nuevo contacto")
        print("2. Borrar un contacto")
        print("3. Buscar un contacto")
        print("4. Mostrar toda la agenda")
        print("5. Salir")
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            agenda_test.nuevo_contacto()
        elif opcion == 2:
            agenda_test.borrar_contacto()
        elif opcion == 3:
            agenda_test.buscar_contacto()
        elif opcion == 4:
            agenda_test.mostrar_agenda()
        elif opcion == 5:
            agenda_test.guardar_agenda()   
            print("Saliendo de la agenda")
            sys.exit()  
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")


agenda_test = Agenda()
menu_agenda()

if __name__ == "__main__":
    menu_agenda()

