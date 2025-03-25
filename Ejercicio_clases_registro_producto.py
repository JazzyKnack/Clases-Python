# Ejercicio 7: Registro de productos
# Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
# Añade un método que calcule el valor total del inventario (precio × cantidad).

class Producto: # Se crea la clase Producto
    
    def __init__(self): # Constructor para iniciar la clase
        self.inventario = {} # Diccionario vacío
        
    def añadir_productos(self): # Método para añadir productos
        insert = True
        while insert is True: # Bucle while para ir añadiendo productos
            self.nombre = input("Introduzca el nombre del producto: ") # Input para introducir el nombre del producto
            self.precio = float(input("Introduzca el precio del producto: ")) # Input para introducir el precio del producto
            self.cantidad = int(input("Introduzca la cantidad del producto: ")) # Input para introducir la cantidad del producto
            atributos_inventario = {"Precio":self.precio, "Cantidad": self.cantidad}
            self.inventario[self.nombre] = atributos_inventario # Agrega el elemento al diccionario
            print() # Separación
            if (input("¿Desea registrar otro producto? S/N: ")).lower() == "n": # Preguntar si se quieren añadir más productos
                insert = False

    def mostrar_inventario(self): # Método para mostrar el inventario
        print("\nInventario:") # Título
        for nombre, datos in self.inventario.items(): # Bucle for para recorrer el inventario
            print(f"\nNombre: {nombre} | Precio: {datos['Precio']} | Cantidad: {datos['Cantidad']}") # Imprimir el inventario


    def calculo_total(self): # Método para calcular el total del inventario
        total = 0 # Variable total comienza en 0
        for nombre, datos in self.inventario.items(): # Bucle for para calcular el valor total de los productos del inventario
            precio = datos["Precio"]
            cantidad = datos["Cantidad"]
            total += precio * cantidad
        print(f"\nEl valor total del inventario es {total}") # Imprimir el valor total del inventario


# Ejemplo de uso
producto1 = Producto()
producto1.añadir_productos()
producto1.mostrar_inventario()
producto1.calculo_total()

