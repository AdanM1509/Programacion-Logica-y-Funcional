# Felipe Carrillo Puerto a 28 de abril del 2026
# ADAN ADAIR MOO NOH - 8B


# Ejercicio 1 Presentacion Personal


nombre = "Adan"
edad = 22
ciudad = "Felipe Carrillo Puerto"
es_estudiante = True

print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Vivo en:", ciudad)
print("¿Soy ISC?:", es_estudiante)

mensaje = "Hola, me llamo " + nombre + ", tengo " + str(edad) + " años, vivo en " + ciudad + " y soy ISC: " + str(es_estudiante) + "."
print(mensaje)



# Ejercicio 2 Casa de cambio

tasa_de_cambio = 19.00

cantidad_usd = float(input("¿Cuántos USD tienes?: "))

cantidad_mxn = cantidad_usd * tasa_de_cambio

print(str(cantidad_usd) + " USD = " + str(cantidad_mxn) + " MXN")




# Ejercicio 3 ¿Quien es mayor de Edad?


nombre1 = input("Nombre de la primera persona: ")
edad1 = int(input(f"Edad de {nombre1}: "))


nombre2 = input("Nombre de la segunda persona: ")
edad2 = int(input(f"Edad de {nombre2}: "))

if edad1 > edad2:
    diferencia = edad1 - edad2
    print(f"\n{nombre1} es mayor que {nombre2} por {diferencia} años.")
else:
    diferencia = edad2 - edad1
    print(f"\n{nombre2} es mayor que {nombre1} por {diferencia} años.")




#Ejercicio 4 Boleta de calificaciones

participacion = float(input("Participación (0-100): "))
trabajos = float(input("Trabajos (0-100): "))
examen_final = float(input("Examen final (0-100): "))

nota_final = (participacion * 0.20) + (trabajos * 0.30) + (examen_final * 0.50)

print(f"\nCALIFICACIÓN FINAL: {nota_final:.2f}")



# Ejercicio 5 Pin de acceso 


pin = input("Ingresa tu PIN de 4 dígitos: ")


es_valido = True
errores = []

if len(pin) != 4 or not pin.isdigit():
    es_valido = False
    errores.append("Debe tener exactamente 4 dígitos numéricos.")
else:
    
    if pin[0] == "0":
        es_valido = False
        errores.append("No puede empezar con 0.")

    
    if pin[0] == pin[1] or pin[1] == pin[2] or pin[2] == pin[3]:
        es_valido = False
        errores.append("No puede tener números repetidos consecutivos.")

    if pin == "1234" or pin == "0123" or pin == "2345" or pin == "3456" or \
       pin == "4567" or pin == "5678" or pin == "6789":
        es_valido = False
        errores.append("Está en secuencia ascendente.")
    
    if pin == "4321" or pin == "3210" or pin == "5432" or pin == "6543" or \
       pin == "7654" or pin == "8765" or pin == "9876":
        es_valido = False
        errores.append("Está en secuencia descendente.")


if es_valido:
    print("✓ PIN válido")
else:
    print(f"✗ PIN inválido: {', '.join(errores)}")




# Ejercicio 6 Tabla de multiplicar

numero = int(input("¿Tabla de qué número? (1-12): "))


if numero < 1 or numero > 12:
    print("Error: El número debe estar entre 1 y 12.")
else:
    
    print(f"Tabla del {numero}")
    
    
    for i in range(1, 11):
        
        print(f"{numero} x {i} = {numero * i}")



# Ejercicio 7 Numeros pares e impares

inicio = int(input("¿Desde qué número?: "))
fin = int(input("¿Hasta qué número?: "))


if inicio >= fin:
    print("Error: El número inicial debe ser menor al número final.")
else:
   
    pares = []
    impares = []

    
    for num in range(inicio, fin + 1):
        
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    
    print(f"Números PARES: {', '.join(map(str, pares))}")
    print(f"Números IMPARES: {', '.join(map(str, impares))}")