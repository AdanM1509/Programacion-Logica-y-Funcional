# 04 - functions

# Adan Adair Moo Noh 8B

from os import system
if system("clear") != 0: system("cls")

#ejemplo de una funcion
def saludar():
    print("hola")



# ejemplo de una funcion con parametro

def saludar_a(nombre):
    print("hola {nombre}:")

saludar_a("estudiante")

saludar_a("jefa")

saludar_a("profesor")



#funciones con mas parametros

def suma(a, b):
    suma = a + b
    return suma

result = suma(2, 3)
print(result)

#documento las dunciones con docstring
def restar(a, b):
    """resta dos numeros y devuelve el resultado"""
    return a- b

#parametro por defecto

def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2))

print(multiplicar(2, 3))

#argumento por defecto

def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"soy {nombre}, tengo{edad}, años y me indetifico como {sexo}")

    describir_persona(1, 25, "gato")
    describir_persona("carlos", 25, "pajaro")
    describir_persona("personas", "ingeniero", 39)


#agrumento por clave
#parametro nombrado

describir_persona(sexo="perro", nombre="reyes", edad=25)
describir_persona(sexo="mujer", nombre="alaejandri", edad=22)