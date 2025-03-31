# Ejercicio 13: Rectángulo
# Crea una clase Rectangulo con atributos para ancho y alto.
# Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.

import sys # Importamos el módulo sys

class Rectangulo: # Creamos la clase Rectangulo

    def __init__(self): # Iniciamos el constructor
        print("Programa para calcular área y perímetro de un rectángulo.") # Mostrar mensaje en pantalla antes de introducir los datos
        
        while True: # Bucle while para pedir los datos al usuario
            try:
                self.ancho = float(input("Introduzca el ancho del rectángulo en metros: ")) # Se pide al usuario que introduzca el ancho del rectángulo
                if self.ancho <= 0: # Si el ancho introducido es menor o igual a cero
                    raise ValueError("Error: El ancho debe ser un número positivo.") # Mostrar mensaje de error
            
                self.alto = float(input("Introduzca el alto del rectángulo en metros: ")) # Se pide al usuario que introduzca el alto del rectángulo
                if self.alto <= 0: # Si el alto introducido es menor o igual a cero
                    raise ValueError("Error: El alto debe ser un número positivo.") # Mostrar mensaje de error
            
                break # Si todo es correcto, salimos del bucle.
            except ValueError as e:
                print(e) # Muestra el mensajde de error correspondiente.
            except Exception:
                print("Error: Introduzca un valor numérico válido.") # Mostrar mensaje de error

    def calculo_area(self): # Método para calcular el área del rectángulo
        self.area = self.ancho * self.alto # Fórmula para calcular el área
        return f"\nEl área del rectángulo es de: {self.area} metros." # Devuelve el resultado del área

    def calculo_perimetro(self): # Método para calcular el perímetro del rectangulo
        self.perimetro = self.ancho * 2 + self.alto * 2 # Fórmula para calcular el perímetro
        return f"\nEl perímetro del rectángulo es de: {self.perimetro} metros." # Devuelve el resultado del perímetro
    
pruebarectangulo = Rectangulo() # Creamos una instancia de la clase Rectangulo()

def menu_rectangulo(): # Función para ejecutar el menúde opciones del programa

    while True: # Bucle while para que se ejecute siempre el menu de opciones
        print("\n###################################")
        print("# Programa para calcular el área  #")
        print("# y el perímetro de un rectángulo #")
        print("###################################\n")
        print("Menú de opciones: ")
        print("Opción 1. Calcular área del rectángulo.") # Opción 1
        print("Opción 2. Calcular el perímetro del rectángulo.") # Opción 2
        print("Opción 3. Salir del programa.") # Opción 3
        
        opcion = input("\nSeleccione una opción del 1 al 3: ") # Se pide al usuario que selecione una opción

        if opcion == "1": # Si la opción es igual a uno
            print(pruebarectangulo.calculo_area()) # Imprimir por pantalla el método calculo_area
        elif opcion == "2": # Si la opción es igual a dos
            print(pruebarectangulo.calculo_perimetro()) # Imprimir porpantalla el método calculo_perimetro
        elif opcion == "3": # Si la opción es igual a tres
            print("Saliendo del programa.") # Mostrar mensaje de salida
            sys.exit() # Sale del programa
        else:
            print("\nOpción inválida: Seleccione una opción del 1 al 3: ") # Si no se selecciona ninguna de las opciones disponibles, muestra el error por pantalla

if __name__ == "__main__": # Si el script se ejecuta directamente
    menu_rectangulo() # Llamamos a la función menu_rectangulo()




    
