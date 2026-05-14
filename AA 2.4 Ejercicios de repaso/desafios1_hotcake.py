# ADAN ADAIR MOO NOH 8B

def preparar_hotcake():
    return "🧇"

def ordenar_hotcakes(numero_hotcakes):
    piezas_hotcakes = [preparar_hotcake() for _ in range(numero_hotcakes)]
    return piezas_hotcakes

hotcakes_familia=ordenar_hotcakes(int(input('¿Cuantos son en tu familia?')))

print(hotcakes_familia)


