# Hacer una aplicación para tener una agenda de teléfonos. crear la clase agenda.
# Los teléfonos se guardarán en un diccionario con clave: nombre del contacto y valor:Teléfono
# Necesitamos los siguientes métodos:
#   - __init__ (por supuesto que siempre hace falta)
#   - Método para introducir nuevo contacto
#   - Método para borrar un contacto (por nombre)
#   - Método para buscar un contacto (por nombre)
#   - Método para mostrar toda la agenda

class Agenda:

    def __init__(self):
        self.phonebook = {}

    def nuevo_contacto(self):
        self.nombre = input("Introduzca su nombre: ")
        self.telefono = int(input("Introduzca su número de teléfono: "))
        self.phonebook [self.nombre]=self.telefono
        print(f"Se ha agregado a la agenda el contacto {self.nombre} con el número de teléfono {self.telefono}")

    def borrar_contacto(self):
        self.contactoaborrar = input("Introduzca el contacto que desea eliminar: ")
        del self.phonebook[self.contactoaborrar]
        print(f"Se ha borrado el contacto {self.contactoaborrar}")
    
    def consultar_contacto(self):
        self.buscarcontacto = input("Introduzca el nombre del contacto que desea buscar: ")
        if self.buscarcontacto in self.phonebook:
            for self.buscarcontacto in self.phonebook.items():
                print(self.phonebook)
        else:
            print("El contacto introducido no se encuentra en la agenda")


