print("Pizzería La Beata")

pizzas_disponibles = ["Margarita", "Pepperoni", "4 Quesos"]
precio_margarita = 5.30
precio_pepperoni = 6.50
precio_4quesos = 6.10
precios_pizzas = [precio_margarita, precio_pepperoni, precio_4quesos]

extras = ["Extra de queso", "Extra de bacon", "Extra de champiñones"]
precio_extra_queso = 1.50
precio_extra_bacon = 2.00
precio_extra_champinones = 1.25
precios_extras = [precio_extra_queso, precio_extra_bacon, precio_extra_champinones]

try:
    dinero = float(input("¿Cuanto dinero puedes gastar? "))
except ValueError:
    print("Error: Por favor, introduce un número válido.")
    exit()

print(f"Tienes {round(dinero, 2):.2f}$")

for i, pizzas in enumerate(pizzas_disponibles):
    precio_actual = precios_pizzas[i]
    print(f"{i + 1}. {pizzas} -> {round(precio_actual, 2):.2f} $")

try:
    opcion_pizza = int(input("\nElige una opción de pizza (número): ")) - 1
    if 0 <= opcion_pizza < len(pizzas_disponibles):
        nombre_pizza = pizzas_disponibles[opcion_pizza]
        precio_pizza_elegida = precios_pizzas[opcion_pizza]
        precio_acumulado = round(precio_pizza_elegida, 2)
        saldo_restante = round(dinero - precio_acumulado, 2)
        print(f"Precio actual: {precio_acumulado:.2f}$ | Saldo restante: {saldo_restante:.2f}$")
    else:
        print("Opción no válida, el programa dejará de ejecutarse")
        exit()
except ValueError:
    print("Por favor, introduce un número válido.")
    exit()

extras_elegidos = []
precios_extras_elegidos = []

while True:
    print("\n--- INGREDIENTES EXTRA ---")
    for i, extra in enumerate(extras):
        print(f"{i + 1}. {extra} -> {round(precios_extras[i], 2):.2f}$")
    print("0. Terminar / Pagar directamente")

    try:
        opcion_extra = int(input("Elige un ingrediente extra (o 0 para finalizar): "))
        if opcion_extra == 0:
            break
        elif 1 <= opcion_extra <= len(extras):
            indice_menos = opcion_extra - 1
            extras_elegidos.append(extras[indice_menos])
            precios_extras_elegidos.append(precios_extras[indice_menos])
            
            precio_parcial = round(precio_pizza_elegida + sum(precios_extras_elegidos), 2)
            saldo_parcial = round(dinero - precio_parcial, 2)
            print(f"-> Añadido. Precio acumulado: {precio_parcial:.2f}$ | Saldo restante: {saldo_parcial:.2f}$")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Por favor, introduce un número válido.")

precio_total = round(precio_pizza_elegida + sum(precios_extras_elegidos), 2)
cambio = round(dinero - precio_total, 2)

if cambio >= 0:
    print("\n--- Su Pedido —")
    print(f"El total de su pedido es {precio_total:.2f}$")
    print(f"Su cambio de {dinero:.2f}$ es: {cambio:.2f}$")
    print()
    print(f"-{nombre_pizza} {precio_pizza_elegida:.2f}$")
    for a in range(len(extras_elegidos)):
        print(f"-{extras_elegidos[a]} {precios_extras_elegidos[a]:.2f}$")
    print()
    print("Gracias por su visita")
else:
    print("\n----------------------------------------")
    print(f"No tienes suficiente dinero (El total es {precio_total:.2f}$ y tienes {dinero:.2f}$).")
    print("Por favor, vuelve a empezar.")