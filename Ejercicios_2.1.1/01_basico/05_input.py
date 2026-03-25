#Adan Adair Moo Noh 8B

# 05-Entrada de usuario (input()) - Versión simplificada


from os import system
if system("clear") !=0: system("cls")

nombre = input("Hola, ¿cómo te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿Cúantos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")