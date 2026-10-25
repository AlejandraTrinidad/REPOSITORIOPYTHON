usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for i in usuarios:
    if i in administradores:
        print(f"{i} es administrador")
    else:
        print(f"{i} no es administrador")