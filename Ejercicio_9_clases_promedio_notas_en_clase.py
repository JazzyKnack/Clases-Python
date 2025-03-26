class Notas:

    def __init__(self, notas = [5]):
        self.notas = notas

    def meter_notas(self):
        try:
            nueva_nota = int(input("Introduzca nota: "))
            if nueva_nota>=0 and nueva_nota<=10:
                self.notas.append(nueva_nota)
            else:
                return self.meter_notas()
        except Exception:
            print("No se pueden meter las notas")
            return self.meter_notas()
        
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def maxima(self):
        return max(self.notas)
    
listado_calif = [6,5,7,3,10,4.5,8.2]

fulanito = Notas(listado_calif)
print(f"La media de Fulanito es {round(fulanito.promedio(),2)}")

menganito = Notas()
print(f"La media de Fulanito es {round(menganito.promedio(),2)}")