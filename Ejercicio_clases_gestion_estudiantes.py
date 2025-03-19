# Ejercicio 5: Gestión de estudiantes
# Crea una clase Estudiante con atributos para nombre, edad y calificación.
# Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación 
# mayor o igual a 6).

class Estudiante: # Definimos la clase Estudiante

    def __init__(self, nombre, edad, calificacion): # Creamos el constructor con los atributos nombre, edad y calificación
        self.nombre = nombre 
        self.edad = edad
        self.calificacion = calificacion

    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self,edad):
        self.edad = edad

    def get_edad(self):
        return self.edad
    
    def set_calificacion(self,calificacion):
        self.calificacion = calificacion

    def get_calificacion(self):
        return self.calificacion
    
    def aprobar_asignatura(self):
        
        if self.calificacion >= 6:
            print(f"El alumno {self.nombre} ha aprobado con una calificación de {self.calificacion}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con una calificación de {self.calificacion}")

estudiante1 = Estudiante("Alberto",38,7.5)
estudiante2 = Estudiante("Ana",42,3.7)

print(estudiante1.get_nombre())
print(estudiante1.get_edad())
print(estudiante1.get_calificacion())
print(estudiante1.aprobar_asignatura())

print(estudiante2.get_nombre())
print(estudiante2.get_edad())
print(estudiante2.get_calificacion())
print(estudiante2.aprobar_asignatura())

