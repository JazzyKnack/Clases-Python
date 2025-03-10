# Crea un clase "Alumno" en la que todos tengan:
# Nombre, Apellidos, Edad
# Crea los setter y getter de esos atributos.
# Crea un metodo que me diga si el alumno es mayor de edad


class Alumno:
 

    def __init__(self):
        self.nombre = None
        self.apellidos = None 
        self.edad = int

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def set_apellidos(self, apellidos):
        self.apellidos = apellidos
    
    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre
    
    def get_apellidos(self):
        return self.apellidos
    
    def get_edad(self):
        return self.edad
    
    def mayoria_edad(self):
        if self.edad > 18:
            print(f"El alumno {self.nombre} {self.apellidos} es mayor de edad")
        else:
            print(f"El alumno {self.nombre} {self.apellidos} es menor de edad")

alumno1 = Alumno()

alumno1.set_nombre("Alberto")
print(alumno1.get_nombre())

alumno1.set_apellidos("Mota Alvarado")
print(alumno1.get_apellidos())

alumno1.set_edad(38)
print(alumno1.get_edad())

alumno1.mayoria_edad()

alumno2 = Alumno()
alumno2.set_nombre("Juan")

