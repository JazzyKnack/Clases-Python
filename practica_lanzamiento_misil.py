# Elabora un programa para el cálculo de el lanzamiento de un misil. Para empezar hay que importar "math" para poder usar las fórmulas que se dan más adelante. 
# Se creará la clase "Lanzamiento" y tendrá varios métodos: Método para establecer el ángulo de lanzamiento ("setter"). Método para establecer la velocidad ("setter"). 
# Para los dos datos anteriores también hacer métodos para consultar el valor ("gettters") La gravedad es una variable que va en el código (ej. gravedad = 9.81) 
# Un método que realice el cálculo del alcance y la altura máxima y nos imprima por pantalla los resultados El código python de las fórmulas del método que realiza los cálculos son: 
# angulo_rad = math.radians(angulo) # convierte ángulo de grados a radianes 
# alcance = (velocidad**2) * math.sin(2*angulo_rad) / gravedad 
# altura_max = (velocidad**2) * (math.sin(angulo_rad)**2) / (2*gravedad) 
# Plus de excelencia: Hacer un menú que tenga las opciones de establecer los datos, consultarlos y realizar el cálculo del lanzamiento. (se puede mantener el menú siempre corriendo con un "while True" por ejemplo)

import math

class Lanzamiento:
    def __init__(self):
        self.angulo = None
        self.velocidad = None
        self.gravedad = 9.81
        
    def set_angulo(self, angulo):
        self.angulo = angulo
    
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad
    
    def get_angulo(self):
        return self.angulo
    
    def get_velocidad(self):
        return self.velocidad
    
    def calcular_lanzamiento(self):
        if self.angulo is None or self.velocidad is None:
            print("Por favor, establece el ángulo y la velocidad primero.")
            return
        else:
            angulo_rad = math.radians(self.angulo) # convierte ángulo de grados a radianes
            alcance = (self.velocidad**2) * math.sin(2*angulo_rad) / self.gravedad
            altura_max = (self.velocidad**2) * (math.sin(angulo_rad)**2) / (2*self.gravedad)
        
            print(f"Alcance: {round(alcance, 2)} metros")
            print(f"Altura máxima: {round(altura_max, 2)} metros")
        

def ejecutar_programa():
    lanzamiento = Lanzamiento()
    
    while True:
        
        print("\n--- Menú de Lanzamiento de Misil ---")
        print("1. Establecer ángulo de lanzamiento")
        print("2. Establecer velocidad de lanzamiento")
        print("3. Consultar ángulo de lanzamiento")
        print("4. Consultar velocidad de lanzamiento")
        print("5. Calcular lanzamiento")
        print("6. Salir del programa")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            angulo = float(input("Introduce el ángulo de lanzamiento (en grados): "))
            lanzamiento.set_angulo(angulo)
        
        elif opcion == "2":
            velocidad = float(input("Introduce la velocidad de lanzamiento (en m/s): "))
            lanzamiento.set_velocidad(int(velocidad))
         
        elif opcion == "3":
            angulo = lanzamiento.get_angulo()
            if angulo is not None:
                print(f"El ángulo de lanzamiento es: {angulo} grados")
            else:
                print("El ángulo de lanzamiento no ha sido establecido.")
        elif opcion == "4":
            velocidad = lanzamiento.get_velocidad()
            if velocidad is not None:
                print(f"La velocidad de lanzamiento es: {velocidad} m/s")
            else:
                print("La velocidad de lanzamiento no ha sido establecida.")
        elif opcion == "5":
            lanzamiento.calcular_lanzamiento()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
            
# Ejecutar el programa llamando a la función ejecutar_programa()
ejecutar_programa()
    
    
    