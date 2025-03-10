
num=int(input("Introduzca un número: "))

def tabla(num):
    for i in range(1,11):
        print(str(num) + "x" +str(i) + "=" + str(num*i))
        print(f"{num}x{i}={num*i}")
        print(" ")
        
tabla(num)

print(f"El número elegido por el usuario fue el {num}")

        