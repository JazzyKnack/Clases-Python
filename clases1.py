

class Militar:
    empleo="Aspirante"
    nombre="USTED!!!"
    edad=int()

    def __init__(self):
        pass

    def saludo(self):
        print("A sus órdenes, buenos días!")

    def dalenombre(self,name):
        self.nombre = name

    def dimenombre(self):
        print(f"El militar se llama {self.nombre}")

    def daleempleo(self,rank):
        self.empleo = rank

    def dimeempleo(self):
        print(f"Su militar es {self.empleo}")

    def setedad(self, age):
        self.edad = age

    def dimeedad(self):
        print(f"Su militar tiene {self.edad} años")

    def cumple(self):
        self.edad += 1

militar1 = Militar()
militar1.dalenombre("Maverick")
militar1.daleempleo("Capitan de Corneta")
militar1.setedad(21)

militar1.dimenombre()
militar1.dimeempleo()
militar1.saludo()
militar1.dimeedad()
militar1.cumple()
militar1.dimeedad()




