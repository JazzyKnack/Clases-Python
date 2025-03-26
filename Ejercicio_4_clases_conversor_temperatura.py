# Ejercicio 4: Conversor de temperaturas 
# Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa. 
# Usa un constructor para inicializar una temperatura base.

class ConversorTemperatura: # Clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.

    def __init__(self, temperatura): # Constructor que inicializa la temperatura base.
        self.temperatura = temperatura # Atributo temperatura

    def celsius_a_fahrenheit(self): # Método para convertir de Celsius a Fahrenheit.
        return self.temperatura * 9/5 + 32 # Devuelve la temperatura en Fahrenheit.
    
    def fahrenheit_a_celsius(self): # Método para convertir de Fahrenheit a Celsius.
        return (self.temperatura - 32) * 5/9 # Devuelve la temperatura en Celsius.
    
# Creamos un objeto de la clase ConversorTemperatura con una temperatura base de 0 grados Celsius.
conversor = ConversorTemperatura(0)

def menu_temperaturas(): # Función que muestra un menú de opciones para convertir temperaturas.
    
    while True: # Bucle while para que el menú se muestre siempre.
        print("*****************************") 
        print("* Conversor de temperaturas *")
        print("*****************************")
        print("Menú de opciones: ") # Menú de opciones.
        print("¿Qué conversión deseas realizar?")
        print("1. Convertir de Celsius a Fahrenheit") # Opción 1: Convertir de Celsius a Fahrenheit.
        print("2. Convertir de Fahrenheit a Celsius") # Opción 2: Convertir de Fahrenheit a Celsius.
        print("3. Salir") # Opción 3: Salir del programa.
        opcion = int(input("Introduce una opción: ")) # Se pide al usuario que introduzca una opción.
    
        if opcion == 1: # Si la opción es 1, se convierte de Celsius a Fahrenheit.
            print(f"La temperatura en Fahrenheit es: {conversor.celsius_a_fahrenheit()}ºF") # Se muestra la temperatura en Fahrenheit.
        elif opcion == 2: 
            print(f"La temperatura en Celsius es: {conversor.fahrenheit_a_celsius()}ºC") # Si la opción es 2, se convierte de Fahrenheit a Celsius.
        elif opcion == 3:
            print("Fin del programa") # Si la opción es 3, se muestra un mensaje de fin del programa.
            break # Se sale del bucle. 
        else:
            print("Opción no válida. Por favor elija una opción válida.") # Si la opción no es válida, se muestra un mensaje de error.  
            menu_temperaturas() # Si la opción no es válida, se vuelve a mostrar el menú de opciones.

menu_temperaturas() # Llamada a la función menu_temperaturas(). 