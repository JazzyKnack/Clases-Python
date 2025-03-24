# Ejercicio 7: Registro de productos
# Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
# Añade un método que calcule el valor total del inventario (precio × cantidad).

class Producto: # Se crea la clase Producto
    
    def __init__(self): # Constructor para iniciar la clase
        self.inventario = {} # Diccionario vacío
        
    def añadir_productos(self): # Método para añadir productos
        insert = True
        while insert is True:
            self.nombre = input("Introduzca el nombre del producto: ") # Input para introducir el nombre del producto
            self.precio = float(input("Introduzca el precio del producto: ")) # Input para introducir el precio del producto
            self.cantidad = int(input("Introduzca la cantidad del producto: ")) # Input para introducir la cantidad del producto
            atributos_inventario = {"Precio":self.precio, "Cantidad": self.cantidad}
            self.inventario[self.nombre] = atributos_inventario # Agrega el elemento al diccionario
            print() # Separación
            if (input("¿Desea registrar otro producto? S/N: ")).lower() == "n": # Preguntar si se quieren añadir más productos
                insert = False

    def mostrar_inventario(self): # Método para mostrar el inventario
        print() # Separación
        for self.nombre, valor in self.inventario.items(): # Bucle para recorrer el diccionario
            print("----") # Separación
            self.precio = valor["Precio"]
            self.cantidad = valor["Cantidad"]
            print("Nombre: {} - Precio: {} | Cantidad: {}".format(self.nombre, self.precio, self.cantidad))

    def calculo_total(self):
        total = 0
        for self.nombre, self.cantidad in self.inventario.items():
            total += self.inventario[self.precio] * self.cantidad
            print(total)



    

# Ejemplo de uso
producto1 = Producto()
producto1.añadir_productos()
producto1.mostrar_inventario()
producto1.calculo_total()

