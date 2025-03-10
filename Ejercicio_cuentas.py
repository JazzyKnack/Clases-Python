# Crea una clase Profesor que tenga los siguientes atributos:
# -Asignatura 
# -Salario
# El salario de los profesores es un valor tipo fijo float. Crea getter y setter para cada atributo.
# Crea la clase ProfesorAsociado, que hereda de profesor, pero cuyo salario es el resultado de sus horas de clase multiplicado por el precio por hora
# (se puede "harcodear" el precio).

import random

class Cuenta:

    cuentas_creadas = []
    
    def __init__(self, saldo_inicial):
        
        while True:
            self.numero = random.randint(1000000000, 9999999999)
            if self.numero not in Cuenta.cuentas_creadas:
                self.saldo = saldo_inicial
                self.riesgo = 1
                Cuenta.cuentas_creadas.append(self.numero)
                break
    
    def setnumero(self, num):
        self.numero = num

    def getnumero(self):
        return self.numero
    
    def getsaldo(self):
        return self.saldo
    
    def ingreso(self, cantidad):
        self.saldo += cantidad

    def retirada(self, cantidad):
        self.saldo -= cantidad


cuenta1 = Cuenta(1000)
cuenta2 = Cuenta(1000)
cuenta3 = Cuenta(1000)

print(cuenta1.getnumero())
print(Cuenta.cuentas_creadas)