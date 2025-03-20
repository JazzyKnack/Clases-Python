# Ejercicio 7: Registro de productos
# Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
# Añade un método que calcule el valor total del inventario (precio × cantidad).

class Producto:

    inventario = {}
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        Producto.inventario[nombre] = self

    def agregar_producto(self):
        nomb = input("Introduce el nombre del artículo: ")
        prec = float(input("Introduzca el precio del artículo: "))
        cant = int(input("Introduzca la cantidad del artículo: "))
        Producto.inventario[nomb] = Producto(nomb, prec, cant)

    def calculo_total(self):
        return self.precio * self.cantidad

    def mostrar_inventario(self):
        for nombre, precio, cantidad in Producto.inventario.items():
            print(f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Total: {producto.calculo_total()}")

# Ejemplo de uso
producto1 = Producto("Manzana", 0.5, 100)
producto2 = Producto("Naranja", 0.75, 80)
producto1.agregar_producto()
producto1.mostrar_inventario()