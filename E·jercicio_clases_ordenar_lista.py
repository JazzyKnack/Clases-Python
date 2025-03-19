# Ejercicio 6: Ordenar una lista
# Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
# Luego, intégrala como método en una clase Ordenador.

class Ordenador:

    def __init__(self):
        self.lista = []

    def ordenar_lista(self,lista):
        self.lista = lista
        for i in range(1, len(lista)):
            for j in range(len(lista - i)):
                temp = lista
