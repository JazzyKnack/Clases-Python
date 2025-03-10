# Imprimir la lista de primos del 1 al 100

def es_primo():
    primos=[]
    for i in range(2,101):
        for j in range(2,i-1):
           if i % j == 0:
               break
        else:
            primos.append(i)
    print(primos)

es_primo()

