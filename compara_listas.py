# Realiza una función que compare dos listas y nos diga si son iguales(misma longitud y los elementos de cada lista sean iguales)

lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6,7]

def compara_listas(l1, l2):
    if len(l1) == len(l2):
        for i in range(len(l1)):
                if l1[i] != l2[i]:
                    break
        else:
            print("Son iguales")
            return

    print("No son iguales")

compara_listas(lista1, lista2)







