# Ejercicio 10: Simulador de dado
# Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
# Incluye un método para tirar el dado y otro para mostrar el resultado.
# EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)

import random # Importamos el método random

class Dado: # Creamos la clase Dado

    def __init__(self): # Iniciamos el constructor
        pass

    def tirar_dado_6_caras(self): # Método para tirar dado de 6 caras
        self.dado6 = random.randint(1, 6)  # Se elige una tirada aleatoria entre 1 y 6
        
    def mostrar_resultado_6(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado6}")

    def tirar_dado_2_caras(self): # Método para tirar dado de 2 caras
        self.dado2 = random.randint(1, 2) # Se elige una tirada aleatoria entre 1 y 2
        
    def mostrar_resultado_2(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado2}")

    def tirar_dado_4_caras(self): # Método para tirar dado de 4 caras
        self.dado4 = random.randint(1, 4) # Se elige una tirada aleatoria entre 1 y 4
        
    def mostrar_resultado_4(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado4}")

    def tirar_dado_8_caras(self): # Método para tirar dado de 8 caras
        self.dado8 = random.randint(1, 8) # Se elige una tirada aleatoria entre 1 y 8
        
    def mostrar_resultado_8(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado8}")

    def tirar_dado_10_caras(self): # Método para tirar dado de 10 caras
        self.dado10 = random.randint(1, 10) # Se elige una tirada aleatoria entre 1 y 10
        
    def mostrar_resultado_10(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado10}")

    def tirar_dado_12_caras(self): # Método para tirar dado de 12 caras
        self.dado12 = random.randint(1, 12) # Se elige una tirada aleatoria entre 1 y 12
        
    def mostrar_resultado_12(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado12}")

    def tirar_dado_20_caras(self): # Método para tirar dado de 20 caras
        self.dado20 = random.randint(1, 20) # Se elige una tirada aleatoria entre 1 y 20
        
    def mostrar_resultado_20(self): # Método para mostrar el resultado de la tirada
        print(f"\nEl resultado de la tirada es: {self.dado20}")

tirada = Dado()   

def menu_dados(): # Función para mostrar el menú de opciones
        
    while True: # Bucle while para mostrar el menú de opciones
        print("\n********************")
        print("* Simulador de dados *") # Menú del simulador de dados
        print("**********************")
        print("1. Dado de 2 caras") # Opción 1. Dado de dos caras
        print("2. Dado de 4 caras") # Opción 2. Dado de cuatro caras
        print("3. Dado de 6 caras") # Opción 3. Dado de seis caras
        print("4. Dado de 8 caras") # Opción 4. Dado de ocho caras
        print("5. Dado de 10 caras") # Opción 5. Dado de diez caras
        print("6. Dado de 12 caras") # Opción 6. Dado de doce caras
        print("7. Dado de 20 caras") # Opción 7. Dado de veinte caras
        print("8. Salir") # Opción 8. Salir
        
        opcion = input("\nElige el dado con el que quieres tirar u opción 8 para salir: ") # input para solicitar al jugador elegir dado
        
        if opcion == '1': # Si la opción elegida es uno
            tirada.tirar_dado_2_caras()
            tirada.mostrar_resultado_2()
        elif opcion == '2': # Si la opción elegida es dos
            tirada.tirar_dado_4_caras()
            tirada.mostrar_resultado_4()
        elif opcion == '3': # Si la opción elegida es tres
            tirada.tirar_dado_6_caras()
            tirada.mostrar_resultado_6()
        elif opcion == '4': # Si la opción elegida es cuatro
            tirada.tirar_dado_8_caras()
            tirada.mostrar_resultado_8()
        elif opcion == '5': # Si la opción elegida es cinco
            tirada.tirar_dado_10_caras()
            tirada.mostrar_resultado_10()
        elif opcion == '6': # Si la opción elegida es seis
            tirada.tirar_dado_12_caras()
            tirada.mostrar_resultado_12()
        elif opcion == '7': # Si la opción elegida es siete
            tirada.tirar_dado_20_caras()
            tirada.mostrar_resultado_20()
        elif opcion == '8': # Si la opción elegida es ocho
            print("Saliendo del simulador") # Muestra la salida del programa
            break # Sale del programa
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 8.") # Muestra opción no válida y vuelve a aparecer el menu de opciones

if __name__ == "__main__":
    menu_dados()
    

