# Ejercicio 14: Juego de adivinanza 
# Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random). 
# Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que acierte.

import sys # Importamos el módulo sys
import random # Importamos el módulo random

class Adivinanza: # Creamos la clase Adivinanza

    def __init__(self): # Iniciamos el constructor de la clase
        print("\n**************************************")
        print("* Bienvenido al juego de adivinanza. *") # Mensaje de bienvenida
        print("**************************************\n")
        print("He elegido un número entre 1 y 100. Intente adivinarlo.\n") # Mostrar instrucciones del programa
        self.numero_secreto = random.randint(1, 100) # Se elije un número aleatorio del 1 al 100
        self.intentos_realizados = 0 # Atributo intentos_realizados. Comienza en 0
        self.intentos_maximos= 10 # Atributo intentos_maximos. El máximo es de 10 intentos
        self.numero_adivinado = False # Atributo numero_adivinado. Comienza en False

    def adivinar_numero(self): # Método para adivinar el número secreto

        while not self.numero_adivinado and self.intentos_realizados < self.intentos_maximos: # Mientras que no se adivine el número secreto y los intentos sean menores que el máximo
            
            try: # Método try
                intento = int(input(f"Intento {self.intentos_realizados + 1} / {self.intentos_maximos}: Introduce tu número: ")) # Se pide al usuario que introduzca un número
                if intento < 1 or intento > 100: # Si el número introducido por el usuario es menor que 1 o mayor que 100
                    raise ValueError("Error: El número debe estar entre 1 y 100.") # Mostrar mensaje de error
                
                self.intentos_realizados += 1 # Contador para ir sumando los intentos realizados

                if intento == self.numero_secreto: # Si el intento es igual al número secreto
                    print(f"\n¡Enhorabuena! Ha adivinado el número secreto {self.numero_secreto} en {self.intentos_realizados} intentos.") # Mostrar mensaje ganador
                    self.numero_adivinado = True # El valor del atributo cambia a True
                elif intento < self.numero_secreto: # Si el número del intento es menor al número secreto
                    print("\nMás alto. Intente de nuevo.") # Mostrar pista
                else: # Si el número del intento es mayor al número secreto
                    print("\nMás bajo. Intente de nuevo.") # Mostrar pista
            
            except ValueError as e: # Método except con alias
                print(e) # Mostrar el error
            
            except Exception: # Método except
                print("\nError: Introduzca un valor numérico válido.") # Mostrar error

        if not self.numero_adivinado: # Si se superan los intentos máximos
            print(f"\nLo siento, ha agotado sus {self.intentos_maximos} intentos. El número secreto era el {self.numero_secreto}.") # Mostrar mensaje de intentos superados

def menu_adivinanza(): # Función para el menú del juego
    while True: # Bucle while para mostrar el menú de opciones
        print("\n***********************")
        print("* Juego de Adivinanza *")
        print("***********************\n")
        print("\nMenú de opciones: ")
        print("1. Jugar") # Opción uno
        print("2. Salir") # Opción dos

        opcion = input("\nSeleccione una opción del 1 al 2: ") # Se ppide al usuario que elija una opción

        if opcion == "1": # Si la opción es igual a uno
            jugar_adivinanza = Adivinanza() # Se crea una instancia de la clase Adivinanza()
            jugar_adivinanza.adivinar_numero() # Se llama al método adivinar_numero
        elif opcion == "2": # Si la opción es igual a dos
            print("\nSaliendo del programa. ¡Gracias por jugar!") # Mostrar mensaje de salida del programa
            sys.exit() # Finaliza el programa
        else: # Si se introuce una opción no válida
            print("\nOpción inválida. Por favor, seleccione opción 1 o 2: ") # Mostrar mensaje de opción inválida

if __name__ == "__main__": # Si el scrip se ejecuta directamente
    menu_adivinanza() # Se llama a la función menu_adivinanza()



