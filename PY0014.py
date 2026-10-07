def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debes introducir un número válido.")

numero1 = pedir_numero("Introduce un número: ")
numero2 = pedir_numero("Introduce un número: ")
numero3 = pedir_numero("Introduce un número: ")


media = (numero1 * 0.15) + (numero2 * 0.35) + (numero3 * 0.50)
print(f"La media es: {media:.2f}")