# Ejercicio 2: Contador de palabras.
# Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
# Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.

def contador_de_palabras(texto): # Función que cuenta las palabras de un texto.
    return len(texto.split()) # Devuelve la longitud de la lista de palabras del texto.

class Texto: # Clase que almacena un texto y tiene un método para contar las palabras.
    def __init__(self, texto): # Constructor que inicializa el texto.
        self.texto = texto # Atributo que almacena el texto.

    def contar_palabras(self): # Método que cuenta las palabras del texto.
        return contador_de_palabras(self.texto) # Devuelve el resultado de la función contador_de_palabras.
    
if __name__ == "__main__": # Ejemplo de uso de la clase Texto.
    texto = Texto("Este es un ejemplo de la función contador de palabras.") # Se crea un objeto de la clase Texto con un texto.
    print(f"El texto contiene {texto.contar_palabras()} palabras.") # Se imprime el número de palabras del texto.

