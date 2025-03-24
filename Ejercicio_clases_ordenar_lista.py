# Ejercicio 6: Ordenar una lista
# Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
# Luego, intégrala como método en una clase Ordenador.

class Ordenador: # Clase Ordenador

    def __init__(self): # Método constructor
        self.lista = [] # Lista vacía

    def ordenar_lista(self, lista): # Método para ordenar la lista. Recibe una lista como atributo
        self.lista = lista # Asigna la lista a la lista de la clase
        for i in range(1, len(lista)): # Bucle para recorrer la lista con función len()
            for j in range(len(lista) - i): # Bucle para recorrer la lista con función len() restando el elemento del primer bucle for
                if lista[j] > lista[j + 1]: # Si el elemento actual es mayor que el siguiente
                    temp = lista[j] # Intercambia los elementos
                    lista[j] = lista[j + 1] # Intercambia los elementos
                    lista[j + 1] = temp # Intercambia los elementos
        return self.lista # Devuelve la lista ordenada

ordenador1 = Ordenador() # Instancia de la clase Ordenador
lista_ordenada = ordenador1.ordenar_lista([7, 4, 9, 23, 3, 7, 1, 34]) # Llama al método ordenar_lista con una lista desordenada
print(lista_ordenada) # Imprime la lista ordenada


