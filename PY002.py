# PY0002: Dada una lista de precios (floats), por ejemplo, “1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4”), aplica:
# 10% de descuento a los elementos de índice par
# 20% de descuento a los elementos de índice impar 
# Si el precio es negativo, se saltará ese elemento.
# Actualiza la lista original y ve mostrando por consola los cambios. El formato de salida es: 
# “indice_lista=N, precio_antes=X.XX, precio_después=Y.YY”

lista = [1.0, 1.5, 15.0, 19.99, -2.0, -1.44, 55.4]

for k, v in enumerate(lista):
    if v < 0:
        continue

    precio_antes = v

    if k % 2 == 0:
        precio_despues = v * 0.9
    elif k % 2 != 0:
        precio_despues = v * 0.8

    lista[k] = round(precio_despues, 2)
    print(f"indice_lista={k}, precio_antes={precio_antes:.2f}, precio_después={precio_despues:.2f}")

