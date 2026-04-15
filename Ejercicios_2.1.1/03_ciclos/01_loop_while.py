# 01 - Bucles

from os import system
if system("clear") !=0: system("cls")

print("\n Bucle while:")

contador = 0

while contador <= 5:
    print(contador)
    contador += 1 

print("\n Bucle while con break:")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

print("\n Bucle con continue:")
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(contador)

print("\n Bucle while con else:")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

else:
    print("El bucle ha terminado")


numero = -1
while numero <0:
    numero = int(input("Escribe un numero positivo:"))
    if numero < 0:
        print("El numero debe ser positivo. Intenta otra vez")

print(f"El numero que haz introducido es {numero}")

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo"))
        if numero < 0:
            print("El numero debe ser positivo, Intenta otra vez")
    except:
        print("Lo que introduces debe ser un numero!")

print(f"El numero que has introducido es {numero}")



