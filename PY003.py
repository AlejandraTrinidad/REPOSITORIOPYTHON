# PY0003: Usando listas realiza las siguientes operaciones.:
# Parte A: Parte de una lista vacía de asistentes. Pide nombres por consola y añadelos a la lista hasta que el usuario escriba “fin”.
# Parte B: Muestra cuántas veces aparece un nombre que te indique el usuario.
# Parte C: muestra por consola la primera posición en la que aparece el nombre anterior y elimina esta ocurrencia.
# Parte D: Inserta al inicio (posición 0) un asistente VIP.
# Muestra la lista final.
# Ejemplo:
# Entrada: Juan, Ana, Ana, Luis, fin; consulta “Ana”; VIP “Directora”.
# Salida: count("Ana")=2, index("Ana")=1; tras remove("Ana"): […]; tras insert(0,"Directora"): ["Directora", …]

lista = []
respuesta = ""
while True:
    nombre = input("Escribe el nombre del asistente (o 'fin' para terminar): ")
    if nombre.lower() == "fin":
        break
    lista.append(nombre)

consulta = input("\n¿Qué nombre quieres buscar?: ")
total_apariciones = lista.count(consulta)
print(f'count("{consulta}") = {total_apariciones}')

if consulta in lista:
    posicion = lista.index(consulta)
    print(f'index("{consulta}") = {posicion}')
    lista.remove(consulta)
    print(f'Tras remove("{consulta}"): {lista}')
else:
    print(f'El nombre "{consulta}" no está en la lista.')

vip = input("\nIntroduce el nombre del asistente VIP: ")
lista.insert(0, vip)
print(f'Tras insert(0, "{vip}"): {lista}')
