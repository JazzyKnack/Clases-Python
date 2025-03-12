import json
import os

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
    
    def mostrar_agenda(self):
        if self.contactos:   # Si se pone is True o == True sale que la agenda está vacía.
            for nombre, info in self.contactos.items():    # Si le damos solo nombre recorre las claves y si le damos info también recorre los valores
                print(f"\nNombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        else:
            print("La agenda está vacía")

def menu():
    pass

if __name__ == "__main__":
    menu()


agenda_test = Agenda()
agenda_test.mostrar_agenda()
