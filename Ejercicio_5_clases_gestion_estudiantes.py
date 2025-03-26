# Ejercicio 5: Gestión de estudiantes
# Crea una clase Estudiante con atributos para nombre, edad y calificación.
# Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación 
# mayor o igual a 6).

class Estudiante: # Definimos la clase Estudiante

    def __init__(self, nombre, edad, calificacion): # Creamos el constructor con los atributos nombre, edad y calificación
        self.nombre = nombre # Atributo nombre
        self.edad = edad # Atributo edad
        self.calificacion = calificacion 

    def set_nombre(self,nombre): # Método setter para el atributo nombre
        self.nombre = nombre # Asignamos el valor del parámetro nombre al atributo nombre
    
    def get_nombre(self): # Método getter para el atributo nombre
        return self.nombre # Devolvemos el valor del atributo nombre
    
    def set_edad(self,edad): # Método setter para el atributo edad
        self.edad = edad # Asignamos el valor del parámetro edad al atributo edad

    def get_edad(self): # Método getter para el atributo edad
        return self.edad # Devolvemos el valor del atributo edad
    
    def set_calificacion(self,calificacion): # Método setter para el atributo calificación
        self.calificacion = calificacion # Asignamos el valor del parámetro calificación al atributo calificación

    def get_calificacion(self): # Método getter para el atributo calificación
        return self.calificacion # Devolvemos el valor del atributo calificación
    
    def aprobar_asignatura(self): # Método que determina si el estudiante ha aprobado o suspendido
        if self.calificacion >= 6:  # Si la calificación es mayor o igual a 6.
            return f"El alumno {self.nombre} ha aprobado con una calificación de {self.calificacion}" # Devuelve un mensaje de aprobado.
        else:
            return f"El alumno {self.nombre} ha suspendido con una calificación de {self.calificacion}" # Si no, devuelve un mensaje de suspendido.

estudiante1 = Estudiante("Alberto",38,7.5) # Creamos un objeto de la clase Estudiante con los atributos nombre, edad y calificación.
estudiante2 = Estudiante("Ana",42,3.7) # Creamos un objeto de la clase Estudiante con los atributos nombre, edad y calificación.

print(estudiante1.get_nombre()) # Mostramos el nombre del estudiante 1.
print(estudiante1.get_edad()) # Mostramos la edad del estudiante 1.
print(estudiante1.get_calificacion()) # Mostramos la calificación del estudiante 1.
print(estudiante1.aprobar_asignatura()) # Mostramos si el estudiante 1 ha aprobado o suspendido.

print(estudiante2.get_nombre()) # Mostramos el nombre del estudiante 2.
print(estudiante2.get_edad()) # Mostramos la edad del estudiante 2.
print(estudiante2.get_calificacion()) # Mostramos la calificación del estudiante 2.
print(estudiante2.aprobar_asignatura()) # Mostramos si el estudiante 2 ha aprobado o suspendido.


# Resultado:

# Alberto
# 38
# 7.5
# El alumno Alberto ha aprobado con una calificación de 7.5
# Ana
# 42
# 3.7
# El alumno Ana ha suspendido con una calificación de 3.7