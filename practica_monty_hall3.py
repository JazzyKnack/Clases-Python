#Hacer un juego: Un concurso de la tele, hay tres puertas, una con una oveja, otra vacia y otra con un coche.
#El jugador elegirá una puerta y el presentador abrirá una de las puertas no elegidas que no contiene el coche
#El jugador cambiará o no de manera aleatoria.
#Se levantará una estadística del éxito al ganar el coche tanto para cuando el jugador eligió cambiar de puerta como para cuando eligió no cambiar
#Todo el proceso se ejecutará en automático, se introducirán únicamente el número de iteraciones.

import random

class Concurso:
    def __init__(self):
        pass

    def concursar(self,intentos):
        self.gana_sin_cambio = 0
        self.gana_con_cambio = 0
        self.intentos = intentos
        
        for i in range(0, intentos):
            #Colocar el coche aleatoriamente detrás de una puerta
            posicion_coche = random.randint(0, 2)

            #Concursante elige una puerta aleatoriamente
            eleccion_concursante = random.randint(0, 2)

            #El presentador abre una puerta con una oveja (no puede ser la puerta del coche ni la del concursante)
            while True:
                eleccion_presentador = random.randint(0, 2)
                if eleccion_presentador != posicion_coche and eleccion_presentador != eleccion_concursante:
                    break

            #El concursante decide cambiar de puerta
            if eleccion_concursante != posicion_coche:
                self.gana_con_cambio += 1
            else:
                self.gana_sin_cambio += 1

      
    
    def informe(self):
        print(f"Probabilidad de ganar manteniendo la puerta inicial: {(self.gana_sin_cambio/self.intentos)*100}%")
        print(f"Probabilidad de ganar cambiando de puerta: {(self.gana_con_cambio/self.intentos)*100}%")
    
#Simular el concurso 100 veces
concurso1 = Concurso()
concurso1.concursar(100)
concurso1.informe()

    
        
