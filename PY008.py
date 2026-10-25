# PY0008: crea las siguientes listas usando compresión:
# Crea una lista con los cuadrados de los números del 1 al 20.
# Filtra la lista anterior para que solo contenga los números impares.

compresion = [x*x for x in range(21)]
print(compresion)

compresion2 = [x for x in compresion if x % 2 != 0]
print(compresion2)