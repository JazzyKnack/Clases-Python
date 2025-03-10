class Militar:
    empleo = "Aspirante"
    nombre = "USTED!!!"
    edad = int()

    def __init__(self, habilitacion_seg = "Unclass"):
        self.hps = habilitacion_seg




militar1 = Militar("CTS")
militar2 = Militar()

print(militar1.hps)
print(militar2.hps)