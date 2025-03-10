#Hacer un juego: Un concurso de la tele, hay tres puertas, una con una oveja, otra vacia y otra con un coche.
#El jugador elegirá una puerta y el presentador abrirá una de las puertas no elegidas que no contiene el coche
#El jugador cambiará o no de manera aleatoria.
#Se levantará una estadística del éxito al ganar el coche tanto para cuando el jugador eligió cambiar de puerta como para cuando eligió no cambiar
#Todo el proceso se ejecutará en automático, se introducirán únicamente el número de iteraciones.

import random

class Concurso:
    def __init__(self, iteraciones):
        self.iteraciones = iteraciones
        self.ganar_cambiando = 0
        self.ganar_sin_cambiar = 0
        self.perder_cambiando = 0
        self.perder_sin_cambiar = 0

    def simular(self):
        for _ in range(self.iteraciones):
            # Colocar el coche y las ovejas detrás de las puertas
            puertas = ['oveja', 'oveja', 'coche']
            random.shuffle(puertas)

            # El jugador elige una puerta al azar
            eleccion_jugador = random.randint(0, 2)

            # Determinar qué puerta abre el presentador sin usar bucles
            if puertas[eleccion_jugador] == 'coche':
                # Si el jugador eligió el coche, el presentador puede abrir cualquiera de las otras dos puertas
                puerta_abierta = (eleccion_jugador + 1) % 3 if random.choice([True, False]) else (eleccion_jugador + 2) % 3
            else:
                # Si el jugador eligió una oveja, el presentador debe abrir la otra puerta con oveja
                if puertas[(eleccion_jugador + 1) % 3] == 'oveja':
                    puerta_abierta = (eleccion_jugador + 1) % 3
                else:
                    puerta_abierta = (eleccion_jugador + 2) % 3

            # El jugador decide cambiar o no cambiar de puerta de manera aleatoria
            cambiar = random.choice([True, False])

            if cambiar:
                # El jugador cambia a la puerta restante
                nueva_eleccion = 3 - eleccion_jugador - puerta_abierta
                if puertas[nueva_eleccion] == 'coche':
                    self.ganar_cambiando += 1
                else:
                    self.perder_cambiando += 1
            else:
                # El jugador se queda con su elección original
                if puertas[eleccion_jugador] == 'coche':
                    self.ganar_sin_cambiar += 1
                else:
                    self.perder_sin_cambiar += 1

    def mostrar_estadisticas(self):
        print(f"Ganar cambiando de puerta: {self.ganar_cambiando / self.iteraciones * 100}%")
        print(f"Perder cambiando de puerta: {self.perder_cambiando / self.iteraciones * 100}%")
        print(f"Ganar sin cambiar de puerta: {self.ganar_sin_cambiar / self.iteraciones * 100}%")
        print(f"Perder sin cambiar de puerta: {self.perder_sin_cambiar / self.iteraciones * 100}%")

# Ejemplo de uso
iteraciones = 10000
concurso = Concurso(iteraciones)
concurso.simular()
concurso.mostrar_estadisticas()

    
        
