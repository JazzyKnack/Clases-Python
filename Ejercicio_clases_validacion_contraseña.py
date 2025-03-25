# Ejercicio 8: Validación de contraseña
# Diseña una clase Validador con un atributo para una contraseña.
# Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.add()

class Validador: # Definimos la clase Validador para comprobar 

    def __init__(self):
        self.contraseña = False

    def verificar_contraseña(self):

        while True:
            self.contraseña = input("Introduce una contraseña: ")
        
            if len(self.contraseña) < 8:
                print("La contraseña introducida debe tener al menos 8 caracteres.")
            elif not any(i.isupper() for i in self.contraseña):
                print("La contraseña introducida debe tener al menos una letra mayúscula.")
            elif not any(i.isdigit() for i in self.contraseña):
                print("La contraseña introducida debe tener al menos un número.")
            else:
                print(f"La contraseña {self.contraseña} es válida")
                break

# Ejemplo de uso:

contraseña1 = Validador()
contraseña1.verificar_contraseña()

# Resultados:

# Introduce una contraseña: Armada01
# La contraseña Armada01 es válida

# Introduce una contraseña: armada01
# La contraseña introducida debe tener al menos una letra mayúscula.

# Introduce una contraseña: Armadaespañola
# La contraseña introducida debe tener al menos un número.

        
        
        