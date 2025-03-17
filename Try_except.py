try:
    print(10/0)
except Exception:
    print("Ha ocurrido un error")

finally:
    print("Este bloque se ejecutará siempre")

# En este ejemplo, se intenta dividir 10 entre 0, lo cual generará una excepción. La excepción se captura en el bloque `except`, y se imprime un mensaje de error. 
# Luego, el bloque `finally` se ejecuta siempre, independientemente de si se produjo una excepción o no.

# Salida:
# Ha ocurrido un error
# Este bloque se ejecutará siempre

try:
    print(10/2) # Esto no generará una excepción, por lo que el bloque `except` no se ejecutará
except Exception:
    print("Ha ocurrido un error") # Esto no se imprimirá

finally:
    print("Este bloque se ejecutará siempre") # Esto se imprimirá

# Salida:
# 5.0
# ste bloque se ejecutará siempre

def calculadora(): 

    try:
        x = int(input("Introduce un número: ")) 
        y = int(input("Introduce otro número: "))
        print(x/y)
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero") # Esto imprimirá un mensaje específico para la excepción de división por cero

    except Exception as e:
        print(f"Ha ocurrido un error: {e}") # Esto imprimirá el mensaje de error específico

    finally:
        calculadora() # Esto llamará a la función `calculadora` de nuevo, para que el usuario pueda intentar de nuevo

calculadora() # Esto llamará a la función `calculadora` por primera vez
