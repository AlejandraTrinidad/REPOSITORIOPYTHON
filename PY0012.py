lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

combinacion_lista = [(x, y) for x in lista1 for y in lista2 if (x + y) % 2 == 0]
print(combinacion_lista)