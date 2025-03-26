# Ejercicio 9: Promedio de notas
# Crea una clase Notas con una lista de calificaciones como atributo.
# Implementa un método que calcule el promedio y otro que devuelva la nota más alta. Añade manejo de 
# excepciones para evitar notas inferiores a 0 o superiores a 10.

class Notas: # Se crea la clase Notas con métodos para agregar notas, calcular promedio y devolver la nota más alta

    def __init__(self): # Constructor que inicializa las notas
        self.notas = [] # Atributo notas

    def agregar_nota(self, nota): # Método para agregar notas
        if nota < 0 or nota > 10: # Si la nota es menor que 0 o mayor que 10, se lanza una excepción
            raise ValueError("La nota debe estar entre 0 y 10") # Se lanza una excepción con un mensaje de error
        self.notas.append(nota) # Se añade la nota a la lista de notas

    def promedio(self): # Método para calcular el promedio
        return f"\nEl promedio de las notas es: {sum(self.notas) / len(self.notas)}" # Devuelve la suma de las notas dividida por el número de notas

    def nota_mas_alta(self): # Método para devolver la nota más alta
        return f"\nLa nota más alta es: {max(self.notas)}\n" # Devuelve la nota más alta
    

nota1 = Notas() # Se crea un objeto de la clase Notas
nota1.agregar_nota(5) # Se agregan notas al objeto nota1
nota1.agregar_nota(9) # Se agregan notas al objeto nota1
nota1.agregar_nota(10) # Se agregan notas al objeto nota1
nota1.agregar_nota(8) # Se agregan notas al objeto nota1
nota1.agregar_nota(7) # Se agregan notas al objeto nota1
nota1.agregar_nota(6) # Se agregan notas al objeto nota1
print(nota1.promedio()) # Se llama al método promedio del objeto nota1
print(nota1.nota_mas_alta()) # Se llama al método nota_mas_alta del objeto nota1 
