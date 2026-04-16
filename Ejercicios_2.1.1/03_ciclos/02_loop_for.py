# 02 - Bucles (for)

from os import system
if system("clear") !=0: system("cls")

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "estudiante"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
    print(f"El indice es {idx} y la fruta es {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
     print(f"El loro esta escondido en el indice {idx}")
    break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro": continue

    print(animal)

# comprension de las listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los numeros pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)


###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

print("\n Bucle For Imprimir Números pares")
for num in range(2, 21, 2):
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los numeros usando un bucle for.

print("\n Bucle For Calcular Media de una lista")
numeros = [10, 20, 30, 40, 50]
suma_total = 0

for n in numeros:
    suma_total += n

media = suma_total / len(numeros)
print(f"La media de la lista {numeros} es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el numero maximo en la lista usando un bucle for.

print("\n Bucle For Buscar el máximo")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print(f"El número máximo en la lista es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con mas de 5 letras
# usando un bucle for y list comprehension.

print("\n Bucle For Filtrar por longitud")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

filtradas_for = []
for p in palabras:
    if len(p) > 5:
        filtradas_for.append(p)
print(f"Filtradas con bucle for: {filtradas_for}")

filtradas_comp = [p for p in palabras if len(p) > 5]
print(f"Filtradas con list comprehension: {filtradas_comp}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

print("\n Bucle For Contar palabras por letra")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra_usuario = input("Introduce una letra para buscar: ").lower()
contador = 0

for p in palabras:
    if p.lower().startswith(letra_usuario):
        contador += 1

print(f"Hay {contador} palabras que empiezan con la letra '{letra_usuario}'")