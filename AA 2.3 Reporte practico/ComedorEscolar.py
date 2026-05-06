# ADAN ADAIR MOO NOH 8B
 
#  SISTEMA DE PEDIDOS: COMEDOR ESCOLAR 


# ── PASO 1: Funciones de Primera Clase ──────────────────────────────────────
# Estas funciones devuelven el nombre del producto.
def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"


# ── PASO 2: Lógica de Promoción ──────────────────────────────────────────────
def calcular_promocion(cantidad):
    # Si lleva 3 o más, regalamos postre
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3: Función de Orden Superior ───────────────────────────────────────
def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    """
    preparar_alimento: callback (función)
    cantidad: int
    precio_unitario: int/float
    """
    
    # a) Comprensión de listas para generar las porciones
    # Ejecuta el callback tantas veces como indique la cantidad
    porciones = [preparar_alimento() for _ in range(cantidad)]

    # b) map() + lambda para calcular los precios individuales
    # Genera una lista donde cada elemento es el precio unitario
    precios = list(map(lambda x: precio_unitario, porciones))

    # c) Llamada a la función de promoción
    promocion = calcular_promocion(cantidad)

    # d) Retornamos la tupla con toda la información
    return porciones, precios, promocion


# ── PASO 4: Interacción con el Usuario ──────────────────────────────────────
print("--- Bienvenida a la Cooperativa Escolar ---")

try:
    cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
    cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
    cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

    # Ejecución de las órdenes usando las funciones de paso 1 como callbacks
    # Precios: Pizza $25, Agua $10, Tamal $15
    orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
    orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
    orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)


    # ── PASO 5: Resumen del Pedido ──────────────────────────────────────────────
    print("\n========== RESUMEN DEL PEDIDO ==========")

    # Desempaquetado y muestra de resultados
    for emoji, titulo, orden in [
        ("🍕", "PIZZAS ", orden_pizza),
        ("🥤", "AGUAS  ", orden_agua),
        ("🫔", "TAMALES", orden_tamal)
    ]:
        porciones, precios, promo = orden
        if len(porciones) > 0:
            print(f"\n{emoji} {titulo}  → {porciones}")
            print(f"💲 Precios   → {precios}")
            print(f"🎁 Promo     → {promo if promo else 'Sin promoción'}")
            # Extra: Suma total de la orden
            print(f"💰 Subtotal  → ${sum(precios)}")

    print("\n========================================")
    print("¡Gracias por su compra!")

except ValueError:
    print("Error: Por favor ingresa solo números enteros para las cantidades.")