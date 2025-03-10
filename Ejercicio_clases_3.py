# Crea una clase Profesor que tenga los siguientes atributos:
# -Asignatura 
# -Salario
# El salario de los profesores es un valor tipo fijo float. Crea getter y setter para cada atributo.
# Crea la clase ProfesorAsociado, que hereda de profesor, pero cuyo salario es el resultado de sus horas de clase multiplicado por el precio por hora
# (se puede "harcodear" el precio).

class Profesor:

    def __init__(self, asignatura, salario):
        self.asignatura = asignatura
        self.salario = salario

    def set_asignatura(self,asignatura):
        self.asignatura = asignatura

    def set_salario(self,salario):
        self.salario = salario

    def get_asignatura(self):
        return self.asignatura
    
    def get_salario(self):
        return self.salario
    
class ProfesorAsociado(Profesor):
    precio_por_hora = 40.0
    
    def __init__(self, asignatura, horas_clase):
        super().__init__(asignatura, horas_clase * ProfesorAsociado.precio_por_hora)
        self.__horas_clase = horas_clase

    def get_horas_clase(self):
        return self.__horas_clase

    def set_horas_clase(self, horas_clase):
        self.__horas_clase = horas_clase
        self.set_salario(horas_clase * ProfesorAsociado.precio_por_hora)
    

# Ejemplo de uso:
profesor1 = Profesor("Matemáticas", 3000.0)
print(profesor1.get_asignatura())  # Matemáticas
print(profesor1.get_salario())     # 3000.0

profesor_asociado1 = ProfesorAsociado("Física", 10)
print(profesor_asociado1.get_asignatura())  # Física
print(profesor_asociado1.get_horas_clase()) # 10
print(profesor_asociado1.get_salario())     # 400.0 (10 horas * 40.0 €/hora)