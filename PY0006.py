inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}

copia_inventario = dict.copy(inventario_inicial)
avisos = []

for i in ventas:
    if i not in copia_inventario:
        copia_inventario.setdefault(i, 0)
        avisos.append(f"El código '{i}' no existía y se añadió con stock 0.")

    copia_inventario[i] -= 1


for i, k in reposiciones.items():
    copia_inventario[i] = copia_inventario.get(i, 0) + k


print(len(copia_inventario))
print(sum(copia_inventario.values()))

if avisos:
    for i in avisos:
        print(f"- {i}")
else:
    print("- No se registraron avisos.")

borrar_claves = [codigo for codigo, stock in copia_inventario.items() if stock <= 0]
for codigo in borrar_claves:
    copia_inventario.pop(codigo)

consulta = input("\nIntroduce un código para consultar su stock: ")
if consulta in copia_inventario:
    print(f"Stock de '{consulta}': {copia_inventario[consulta]}")
else:
    print("No existe")

del copia_inventario