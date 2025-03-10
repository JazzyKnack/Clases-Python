# Realiza una función que compare dos listas y nos diga si son iguales(misma longitud y los elementos de cada lista sean iguales)



def comparador(l1, l2):
     if len(l1) != len(l2):
          return "Son diferentes"
     else:
        for indice in range(len(l1)):
             if l1[indice] != l2[indice]:
                  return "Son diferentes"
        return "Son iguales"
     
lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,5,6]

print(comparador(lista1, lista2))