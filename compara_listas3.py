# Realiza una función que compare tres listas y nos diga si son iguales(misma longitud y los elementos de cada lista sean iguales)


lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,8,5,6]
lista3 = []

def compara_listas(l1, l2, l3):
    if len(l1) == len(l2) and len(l1) == len(l3) and len(l2) == len(l3):
        for i in range(len(l1)):
                if l1[i] != l2[i] or l1[i] != l3[i] or l2[i] != l3[i]:
                    break
        else:
            print("Son iguales")
            return

    print("No son iguales")

while True:
    x=int(input("Introduzca dato (para salir escriba -15489): "))
    if x != -15489:
        lista3.append(x)
    else:
         break
        

resultado = compara_listas(lista1, lista2, lista3)
print(resultado)

print(lista3)