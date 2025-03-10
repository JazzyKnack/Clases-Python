""" Hacer una aplicación para tener una agenda de teléfonos. crear la clase agenda.
 Los teléfonos se guardarán en un diccionario con clave: nombre del contacto y valor:Teléfono
 Necesitamos los siguientes métodos:
   - __init__ (por supuesto que siempre hace falta)
   - Método para introducir nuevo contacto
   - Método para borrar un contacto (por nombre)
   - Método para buscar un contacto (por nombre)
   - Método para mostrar toda la agenda"""

class Agenda:

    def __init__(self):
        self.phonebook = {}

    def nuevo_contacto(self):
        nombre = input("Introduzca su nombre: ")
        telefono = int(input("Introduzca su número de teléfono: "))
        self.phonebook [nombre]=telefono
        print(f"Se ha agregado a {nombre} con el número {telefono}")

    def borrar_contacto(self):
        nombre = input("Introduce el nombre del contacto a eliminar: ")
        if nombre in self.phonebook:
            self.phonebook.pop(nombre)
            print(f"Contacto {nombre} eliminado con éxito.")
        else:
            print(f"Contacto {nombre} no encontrado.")
    
    def buscar_contacto(self):
        nombre = input("Introduce el nombre del contacto a buscar: ")
        if nombre in self.phonebook:
            telefono = self.phonebook[nombre]
            print(f"El contacto es {nombre} y su número de teléfono es {telefono}.")
        else:
            print("El contacto introducido no se encuentra en la agenda.")
    
    def mostrar_agenda(self):
        if self.phonebook:
            for nombre, telefono in self.phonebook.items():
                print(f"Nombre: {nombre}, Teléfono: {telefono}")
        else:
            print("La agenda está vacía.")

    def menu_agenda(self):
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
                mi_agenda.nuevo_contacto()
            elif opcion == 2:
                mi_agenda.borrar_contacto()
            elif opcion == 3:
                mi_agenda.buscar_contacto()
            elif opcion == 4:
                mi_agenda.mostrar_agenda()
            elif opcion == 5:
                print("Saliendo de la agenda")
                break    
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")


mi_agenda = Agenda()
mi_agenda.menu_agenda()






