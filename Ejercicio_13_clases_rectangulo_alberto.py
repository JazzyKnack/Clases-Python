# Ejercicio 13: Rectángulo
# Crea una clase Rectangulo con atributos para ancho y alto.
# Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.

import sys # Importamos el módulo sys

class Rectangulo: # Creamos la clase Rectangulo

    def __init__(self): # Iniciamos el constructor
        print("Programa para calcular área y perímetro de un rectángulo.") # Mostrar mensaje en pantalla antes de introducir los datos
        self.ancho = float(input("Introduzca el ancho del rectángulo en metros: ")) # Se pide al usuario que introduzca el ancho del rectángulo
        self.alto = float(input("Introduzca el alto del rectángulo en metros: ")) # Se pide al usuario que introduzca el alto del rectángulo
        if self.ancho <= 0 or self.alto <= 0: # 
            raise ValueError ("Error: Introduzca sólo números positivos.")
        if self.ancho == "" or self.alto == "":
            raise ValueError ("Error: No puede introducir texto.")

    def calculo_Area(self):
        self.area = self.ancho * self.alto
        return f"\nEl área del rectángulo es de: {self.area} metros."

    def calculo_perimetro(self):
        self.perimetro = self.ancho * 2 + self.alto * 2
        return f"\nEl perímetro del rectángulo es de: {self.perimetro} metros."
    
pruebarectangulo = Rectangulo()

def menu_rectangulo():

    while True:
        print("\n###################################")
        print("# Programa para calcular el área  #")
        print("# y el perímetro de un rectángulo #")
        print("###################################\n")
        print("Menú de opciones: ")
        print("Opción 1. Calcular área del rectángulo.")
        print("Opción 2. Calcular el perímetro del rectángulo.")
        print("Opción 3. Salir del programa.")
        
        opcion = input("\nSeleccione una opción del 1 al 3: ")

        if opcion == "1":
            print(pruebarectangulo.calculo_Area())
        elif opcion == "2":
            print(pruebarectangulo.calculo_perimetro())
        elif opcion == "3":
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("\nOpción inválida: Seleccione una opción del 1 al 3: ")

if __name__ == "__main__":
    menu_rectangulo()




    
