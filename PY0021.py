lista = [10, 15 , 100, 40, 35, 353, 400, 40, 500, 420, 340, 115]
print(sorted(lista))
lista_filtrada = [x for x in lista if x != 40]
print(lista_filtrada)
lista_filtrada2 = [x for x in lista if x < 339]
print(lista_filtrada2)