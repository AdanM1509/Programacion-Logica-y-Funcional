# ADAN ADAIR MOO NOH 8B

# Ejercicio 1: Ordenar cafe para el grupo ISC

def preparar_cafe():
    return "cafe"

def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = ordenar_cafe(10)

def preparar_cafe_americano():
    return "cafe americano"

def preparar_cafe_olla():
    return "cafe olla"

def ordenar_cafe(preparar_cafe, numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_americano, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_olla, 12)

print(cafe_grupo_a, cafe_grupo_b)