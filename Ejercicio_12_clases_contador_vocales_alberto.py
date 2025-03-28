# Ejercicio 12: Contador de vocales
# Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
# Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.

import sys # Importamos el módulo sys

class AnalizadorTexto: # Creamos la clase AnalizadorTexto

    def __init__(self): # Iniciamos el constructor
        self.texto = None # Atributo texto

    def contador_vocales(self): # Definimos el método para contar las vocales
        try: 
            self.texto = input("\nIntroduzca una cadena de texto: ") # Se pide al usuario que ingrese una cadena de texto
            self.vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] # Creamos una lista con las vocales
            self.contvocales = 0 # Contador de vocales, comienza en cero

            for i in self.texto: # Bucle for para recorrer el texto
                if i in self.vocales: # Si está contenido en la lista de vocales
                    self.contvocales += 1 # Se van sumando las vocales al contador

            print(f"\nNúmero de Vocales contenidas en el texto: {self.contvocales} ") # Mostrar mensaje
        except Exception as e:
            print(f"Ha ocurrido un error: {e}")

texto1 = AnalizadorTexto() # Creamos una instancia de la clase AnalizadorTexto

def main(): # Función para ejecutar el programa
    while True: # Bucle while para mostrar el menú de opciones
        print("******************************************")
        print("Bienvenido al programa que contabiliza las")
        print("vocales contenidas en una cadena de texto.")
        print("******************************************")      
        print("Menú de opciones") # Mostrar menú de opciones
        print("Opción 1: Introducir cadena de texto.")
        print("Opción 2: Salir del programa.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": # Si la opción es igual a uno
            texto1.contador_vocales() # Se llama al método contador_vocales
        elif opcion == "2": # Si la opción es igual a dos
            print("Saliendo del programa...")
            sys.exit() # Salir del programa
        else:
            print("Opción no válida. Seleccione una opción del 1 al 2.")
        

if __name__ == "__main__": # Si el script se ejecuta directamente
    main() # Llamamos a la función main()