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



###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los numeros del 10 al 1 usando un bucle while.

print("\n Bucle While cuenta atras")
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("\n Bucle While suma de numeros pares")
contador = 1
suma = 0
while contador <= 20:
    if contador % 2 == 0:
        suma += contador
    contador += 1
print(f"La suma total es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

print("\n Bucle While factorial de un numero")
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número entero positivo para su factorial: "))
        if numero < 0:
            print("Debe ser positivo.")
    except:
        print("¡Debe ser un número!")

factorial = 1
aux = numero
while aux > 0:
    factorial *= aux
    aux -= 1
print(f"El factorial de {numero} es {factorial}")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

print("\n Bucle While validacion de contraseña")
password = ""
while len(password) < 8:
    password = input("Introduce una contraseña (min 8 caracteres): ")
    if len(password) < 8:
        print("Contraseña demasiado corta. Intenta otra vez.")

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

print("\n Bucle While tabla de multiplicar")
numero = int(input("Escribe un número para ver su tabla: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\n Bucle While Números primos hasta N")
n = int(input("Escribe un número positivo N: "))
candidato = 2

while candidato <= n:
    es_primo = True
    divisor = 2
    while divisor < candidato:
        if candidato % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        print(f"El número {candidato} es primo")
    
    candidato += 1