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
        else:
            return {}
        
    def mostrar_agenda(self):
        if self.contactos:   # Si se pone is True o == True sale que la agenda está vacía.
            for nombre, info in self.contactos.items():    # Si le damos solo nombre recorre las claves y si le damos info también recorre los valores
                print(f"\nNombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        else:
            print("La agenda está vacía")

    def buscar_contactos(self):
        pass

agenda_test = Agenda()
agenda_test.mostrar_agenda()