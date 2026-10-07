numero = int(input("Introduce un número impar: "))

while numero % 2 == 0:
    try:
        numero = int(input("Introduce un número impar, el que has introducido no lo es: "))
        if numero % 2 == 1:
            print("El número es impar")
            break
    except ValueError:
        print("Debe introducir un número impar")

