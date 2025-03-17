# Ejercicio 1: Calculadora básica con clases
# Crea una clase Calculadora que tenga métodfos para sumar, restar, multiplicar y dividir dos números.
# Incluye un constructor que inicialice los dos números como atributos.add()


class Calculadora: # Creamos la clase
    def __init__(self, num1, num2): # Constructor 
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "No se puede dividir entre 0"

# Instanciamos la clase
test_calculadora = Calculadora(10, 5)
print(test_calculadora.suma())
print(test_calculadora.resta())
print(test_calculadora.multiplicacion())
print(test_calculadora.division())
        
