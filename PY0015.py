# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila el cuarto elemento siempre debe ser el
#  resultado de sumar los tres primeros. Crea un programa que actualice todos los elementos de la cuarta columna para que cumpla esta condición.
# Usa sum(fila)
# Usa slicing [i:j:n]
# matriz = [
#    [1, 1, 1, 3],
#    [2, 2, 2, 7],
#    [3, 3, 3, 9],
#    [4, 4, 4, 13] 
# ]

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13] 
]

for fila in matriz :
    fila[3] = sum(fila[0:3])
    print(fila)
