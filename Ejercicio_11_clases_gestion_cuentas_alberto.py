# Ejercicio 11: Gestión de cuentas bancarias
# Crea una clase CuentaBancaria con atributos para titular y saldo.
# Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.

import sys # Importamos la librería sys

class CuentaBancaria: # Creamos la clase CuentaBancaria

    def __init__(self): # Iniciamos el constructor
        self.titular = None # Atributo titular
        self.saldo = 0 # Atributo saldo que comienza en 0

    def depositar_dinero(self): # Método para depositar dinero en la cuenta
        try: # Establecemos el try
            saldo = float(input("Introduzca el importe que quiere ingresar en la cuenta: ")) # Se pide al usuario que introduzca el importe a ingresar
            self.saldo = saldo # Se añade el saldo al saldo de la cuenta
            print(f"Se ha depositado en la cuenta la cantidad de {saldo} euros") # Mostrar mensaje informativo del saldo ingresado
        except ValueError: # Establecemos el except
            print("Error: Introduce un importe válido para ingresar.") # Mostrar mensaje de error

    def retirar_dinero(self): # Método para retirar dinero de la cuenta
        try: # Establecemos el try
            saldo_retirado = float(input("Introduzca el importe que quiere retirar de la cuenta: ")) # Se pide al usuario el importe que quiere retirar de la cuenta
            if saldo_retirado > self.saldo: # Si el saldo a retirar es mayor que el saldo en cuenta
                raise ValueError ("No hay suficiente saldo") # Mostrar mensaje de error
            self.saldo -= saldo_retirado # Se resta el importe retirado del saldo de la cuenta
            print(f"Se ha retirado de la cuenta la cantidad de {saldo_retirado} euros") # Mostrar mensaje informativo del saldo retirado
        except ValueError as e: # Establecemos el except
            print(f"Operación no válida debido a {e}") # Mostrar mensaje de error

    def mostrar_saldo(self): # Método para consultar el saldo
        print(f"El saldo actual de la cuenta es de {self.saldo} euros") # Mostrar el saldo de la cuenta

titular1 = CuentaBancaria() # Creamos una instancia de la clase CuentaBancaria

def mostrar_menu(): # Función para mostrar el menú de opciones
    print("\n*************************")
    print("*** Bienvenido a BBVA ***")
    print("*************************\n")
    print("1. Consultar el saldo de la cuenta") # Opción 1
    print("2. Ingresar dinero en la cuenta") # Opción 2
    print("3. Retirar dinero de la cuenta") # Opción 3
    print("4. Salir") # Opción 4

def main(): # Función main para ejecutar el menú de opciones
    while True: # Bucle while para ejecutar el menú
        mostrar_menu() # Se llama a la función para mostrar el menú
        opcion = input("Selecciona una opción del 1 al 4: ") # Se pide al usuario que elija una opción
        if opcion == "1": # Si la opción es igual a 1
            titular1.mostrar_saldo() # Se llama al método mostrar_saldo
        elif opcion == "2": # Si la opción es igual a 2
            titular1.depositar_dinero() # Se llama al método depositar_dinero
        elif opcion == "3": # Si la opción es igual a 3
            titular1.retirar_dinero() # Se llama al método retirar_dinero
        elif opcion == "4": # Si la opción es igual a 4
            print("Saliendo de la cuenta") # Mostrar mensaje de salida
            sys.exit() # Sale del programa
        else:
            print("Opción no válida. Seleccione una opción del 1 al 4.") # Si la opción es incorrecta muestra un error y se vuelve al menú

if __name__ == "__main__": # Si el script se ejecuta directamente
    main() # Llamamos a la función main
