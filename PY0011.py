
lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
resultado = [numero for sublista in lista_de_listas for numero in sublista ]
print(resultado)

resultado2 = [numero for sublista in lista_de_listas for numero in sublista if numero % 2 == 0]
print(resultado2)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado3 = [[fila[i] for fila in matriz] for i in range(len(matriz))]
for fila in resultado3:
    print(fila)