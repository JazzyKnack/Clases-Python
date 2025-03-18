# Ejercicio 1: Calculadora básica con clases
# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
# Incluye un constructor que inicialice los dos números como atributos.


class Calculadora: # Clase Calculadora con métodos para sumar, restar, multiplicar y dividir dos números.
    
    def __init__(self, num1, num2): # Constructor que inicializa los dos números como atributos.
        self.num1 = num1 # Atributo num1
        self.num2 = num2 # Atributo num2
        
    def sumar(self): # Método para sumar dos números.
        return self.num1 + self.num2 # Devuelve la suma de los dos números.
    
    def restar(self): # Método para restar dos números.
        return self.num1 - self.num2 # Devuelve la resta de los dos números.
    
    def multiplicar(self): # Método para multiplicar dos números.
        return self.num1 * self.num2 # Devuelve la multiplicación de los dos números.
    
    def dividir(self): # Método para dividir dos números.
        return self.num1 / self.num2 # Devuelve la división de los dos números.
    
    def __str__(self): # Método especial para representar la clase como una cadena de texto.
        return f'Calculadora({self.num1}, {self.num2})' # Devuelve la representación de la clase como una cadena de texto.

def menu(): # Función para mostrar el menú de la calculadora.
        
    while True: # Bucle infinito para mostrar el menú de la calculadora.
        print("\n------------------------------------")
        print("- Calculadora de operaciones básicas -") # Menú de la calculadora.
        print("--------------------------------------")
        print("1. Sumar") # Opción 1. Sumar
        print("2. Restar") # Opción 2. Restar
        print("3. Multiplicar") # Opción 3. Multiplicar
        print("4. Dividir") # Opción 4. Dividir
        print("5. Salir") # Opción 5. Salir
        
        opcion = input("Elige una opción: ") # 
        
        if opcion == '1':
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            calculadora = Calculadora(num1, num2)
            print(f"\nResultado de la suma: {calculadora.sumar()}")
        elif opcion == '2':
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            calculadora = Calculadora(num1, num2)
            print(f"\nResultado de la resta: {calculadora.restar()}")
        elif opcion == '3':
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            calculadora = Calculadora(num1, num2)
            print(f"\nResultado de la multiplicación: {calculadora.multiplicar()}")
        elif opcion == '4':
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            calculadora = Calculadora(num1, num2)
            print(f"\nResultado de la división: {calculadora.dividir()}")
        elif opcion == '5':
            print("\nSaliendo del programa.")
            break
        else:
            print("\nOpción no válida. Por favor, elige una opción del 1 al 5.")

if __name__ == "__main__":
    menu()
     
