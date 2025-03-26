# Ejercicio 3: Lista de números pares 
# Crea una clase Numeros con un atributo que sea una lista de enteros. 
# Incluye un método que devuelva solo los números pares de esa lista. 

class Numeros: # Se crea la Clase Numeros
    
    def __init__(self): # Se inicia el Constructor
        self.lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Se crea la lista de números

    def numeros_pares(self): # 
        pares = [] # Se crea una lista vacía
        for i in self.lista: # Se recorre la lista de números
            if i % 2 == 0: # Se verifica si el número es par
                pares.append(i) # Se añade el número par a la lista pares
        return pares # Se retorna la lista pares
            
numeros = Numeros() # Se crea el objeto numeros
print(numeros.numeros_pares()) # Se imprime la lista de números pares


# Resultado:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 