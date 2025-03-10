# crea la clase "Cuenta". Cada cuenta tendrá un número (diferente a las demás) y un saldo (float)
# El número de cuenta se puede consultar y modificar (getter y setter) pero el saldo sólo puede consultarse (getter).
# Para modificar el saldo tenemos que hacer un ingreso o una retirada.

class Cuenta:
    def __init__(self):
        self.num_cuenta = int
        self.saldo_cuenta = float

    def set_num_cuenta(self, num_cuenta):
        self.num_cuenta = num_cuenta

    def get_num_cuenta(self):
        return self.num_cuenta
    
    def get_saldo_cuenta(self):
        return self.saldo_cuenta
    
    def ingresar_dinero(self):
        saldo_cuenta = float(input("Introduzca el importe que quiere ingresar en la cuenta: "))
        self.saldo_cuenta = saldo_cuenta

    def retirar_dinero(self):
        saldo_actual = float(input("Introduzca el importe que quiere retirar de la cuenta: "))
        self.saldo_cuenta -= saldo_actual

cuenta1 = Cuenta()
cuenta1.set_num_cuenta(54996789)
print(cuenta1.get_num_cuenta())

cuenta1.ingresar_dinero()
cuenta1.retirar_dinero()
print(cuenta1.get_saldo_cuenta())