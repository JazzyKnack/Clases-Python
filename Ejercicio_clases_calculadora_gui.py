# Ejercicio 1: Calculadora básica con clases
# Crea una clase Calculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
# Incluye un constructor que inicialice los dos números como atributos.


import tkinter as tk
from tkinter import messagebox
from Ejercicio_clases_calculadora import Calculadora

class CalculadoraGUI: # Clase Calculadora con métodos para sumar, restar, multiplicar y dividir dos números.
    
    def __init__(self, root): 
        self.root = root 
        self.root.title("Calculadora")
        self.root.geometry("300x400")

        tk.Label(root, text="Número 1:").pack(pady=5)
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=5)

        tk.Label(root, text="Número 2:").pack(pady=5)
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=5)

        tk.Button(root, text="Sumar", command=self.calcular_suma).pack(pady=5)
        tk.Button(root, text="Restar", command=self.calcular_resta).pack(pady=5)
        tk.Button(root, text="Multiplicar", command=self.calcular_multiplicacion).pack(pady=5)
        tk.Button(root, text="Dividir", command=self.calcular_division).pack(pady=5)

        self.resultado_label = tk.Label(root, text="Resultado: ")
        self.resultado_label.pack(pady=20)

    def get_numeros(self):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            return None, None
        
    def calcular_suma(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.sumar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_resta(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.restar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_multiplicacion(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.multiplicar()
            self.resultado_label.config(text=f"Resultado: {resultado}")

    def calcular_division(self):
        num1, num2 = self.get_numeros()
        if num1 is not None:
            calc = Calculadora(num1, num2)
            resultado = calc.dividir()
            self.resultado_label.config(text=f"Resultado: {resultado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()