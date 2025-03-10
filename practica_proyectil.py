import math

def calcular_alcance(velocidad, angulo_rad, gravedad):
    return (velocidad**2) * math.sin(2*angulo_rad) / gravedad

def calcular_altura_max(velocidad, angulo_rad, gravedad):
    return (velocidad**2) * (math.sin(angulo_rad)**2) / (2*gravedad)

def mostrar_resultados(velocidad, angulo, gravedad=9.81):
    angulo_rad = math.radians(angulo)
    alcance = calcular_alcance(velocidad, angulo_rad, gravedad)
    altura_max = calcular_altura_max(velocidad, angulo_rad, gravedad)
    print(f"Para un ángulo de {angulo} grados y una velocidad de {velocidad} m/s:")
    print(f"  - Alcance: {alcance:.2f} metros")
    print(f"  - Altura máxima: {altura_max:.2f} metros")

def calcular_rango_angulos(velocidad, angulo_inicial, angulo_final, incremento, gravedad=9.81):
    resultados = {}
    for angulo in range(angulo_inicial, angulo_final + 1, incremento):
        angulo_rad = math.radians(angulo)
        alcance = calcular_alcance(velocidad, angulo_rad, gravedad)
        altura_max = calcular_altura_max(velocidad, angulo_rad, gravedad)
        resultados[angulo] = {
            "Alcance": alcance,
            "Altura máxima": altura_max
        }
    return resultados

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Calcular alcance y altura máxima para un ángulo específico")
    print("2. Calcular alcance y altura máxima para un rango de ángulos")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            try:
                velocidad = float(input("Introduce la velocidad inicial (m/s): "))
                angulo = float(input("Introduce el ángulo de disparo (grados): "))
                gravedad = input("Introduce la gravedad (opcional, presiona Enter para usar 9.81 m/s²): ")
                gravedad = float(gravedad) if gravedad else 9.81

                mostrar_resultados(velocidad, angulo, gravedad)
            except ValueError:
                print("Error: Introduce valores numéricos válidos.")

        elif opcion == "2":
            try:
                velocidad = float(input("Introduce la velocidad inicial (m/s): "))
                angulo_inicial = int(input("Introduce el ángulo inicial (grados): "))
                angulo_final = int(input("Introduce el ángulo final (grados): "))
                incremento = int(input("Introduce el incremento de ángulo (grados): "))
                gravedad = input("Introduce la gravedad (opcional, presiona Enter para usar 9.81 m/s²): ")
                gravedad = float(gravedad) if gravedad else 9.81

                resultados = calcular_rango_angulos(velocidad, angulo_inicial, angulo_final, incremento, gravedad)
                print("\nResultados para el rango de ángulos:")
                for angulo, valores in resultados.items():
                    print(f"Ángulo: {angulo} grados")
                    print(f"  - Alcance: {valores['Alcance']:.2f} metros")
                    print(f"  - Altura máxima: {valores['Altura máxima']:.2f} metros")
                    print()
            except ValueError:
                print("Error: Introduce valores numéricos válidos.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

if __name__ == "__main__":
    main()