'''
def tabla_multiplicar():
    num= int(input("inserte un número: "))
    for i in range(1,11):
        print(f"{num} X8 {i} = {num*i}")
tabla_multiplicar()
'''
#imprimir la lista de primos del 1 al 100

def es_primo(num):
        if num<2:
             return False
        else:
            for i in range(2,num-1):
                  if num % i == 0:
                       return False
            return True


def lista_primos():
    primos=[]
    for i in range(2,101):
        for j in range(2,i-1):
            if i % j == 0:
                 break
        else:
            primos.append(i)
    print(primos)


