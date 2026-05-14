# ADAN ADAIR MOO NOH 8B

def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def calcular_bonus(num_porciones):
    if num_porciones > 2:
        return "coca gratis"
    else:
        return ""

def tomar_orden(preparar_alimento, num_porciones):
    porciones_alimento = [preparar_alimento() for _ in range(num_porciones)]
    bonus = calcular_bonus(num_porciones)
    return porciones_alimento, bonus


cant_p = int(input('¿Cuantas Pizzas desea ordenar? '))
res_p, bon_p = tomar_orden(preparar_pizza, cant_p)
print(f"Orden: {res_p} Bonus: {bon_p}")

cant_h = int(input('¿Cuantas Hamburguesas desea ordenar? '))
res_h, bon_h = tomar_orden(preparar_hamburguesa, cant_h)
print(f"Orden: {res_h} Bonus: {bon_h}")

cant_hd = int(input('¿Cuantos Hotdog desea ordenar? '))
res_hd, bon_hd = tomar_orden(preparar_hotdog, cant_hd)
print(f"Orden: {res_hd} Bonus: {bon_hd}")