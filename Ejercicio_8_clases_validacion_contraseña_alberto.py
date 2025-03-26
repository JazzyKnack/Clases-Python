# Ejercicio 8: Validación de contraseña
# Diseña una clase Validador con un atributo para una contraseña.
# Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.add()

class Validador: # Definimos la clase Validador con método para verificar contraseña

    def __init__(self): # Constructor que inicializa la contraseña en False
        self.contraseña = False

    def verificar_contraseña(self): # Método para verificar si la contraseña cumple los requisitos

        while True: # Bucle while para introducir la contraseña y verificarla
            self.contraseña = input("Introduce una contraseña que contenga al menos 8 caracteres, una mayúscula y un número: ") # Se pide al usuario que ingrese una contraseña
        
            if len(self.contraseña) < 8: # Si la longitud de la contraseña es menor que 8
                print("La contraseña introducida debe tener al menos 8 caracteres.") # Muestra un mensaje de error
            elif not any(i.isupper() for i in self.contraseña): # Bucle para comprobar si existe alguna letra mayúscula
                print("La contraseña introducida debe tener al menos una letra mayúscula.") # Muestra un mensaje de error
            elif not any(i.isdigit() for i in self.contraseña): # Bucle para comprobar si existe algún número
                print("La contraseña introducida debe tener al menos un número.") # Muestra un mensaje de error
            else:
                print(f"La contraseña {self.contraseña} es válida") # Muestra un mensaje de contraseña correcta
                break # Finaliza el programa

# Ejemplo de uso:

contraseña1 = Validador() # Creamos un objeto de la clase Validador
contraseña1.verificar_contraseña() # Llama al método verificar_contraseña

# Resultados:

# Introduce una contraseña: Armada01
# La contraseña Armada01 es válida

# Introduce una contraseña: armada01
# La contraseña introducida debe tener al menos una letra mayúscula.

# Introduce una contraseña: Armadaespañola
# La contraseña introducida debe tener al menos un número.

        
        
        