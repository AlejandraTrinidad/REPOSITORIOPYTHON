def calculadora():
    while True:
        try:
            entrada1 = input("\nIntroduce el primer número o 'salir': ").strip().lower()
            if entrada1 == 'salir':
                print("Hasta luego")
                break
            num1 = int(entrada1)

            entrada2 = input("Introduce el segundo número o 'salir': ").strip().lower()
            if entrada2 == 'salir':
                print("Hasta luego")
                break
            num2 = int(entrada2)
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            opcion = int(input("Introduce el número de la opción deseada: "))

            if opcion == 1:
                resultado = num1 + num2
                print(f"La suma es: {resultado:.2f}")
            elif opcion == 2:
                resultado = num1 - num2
                print(f"La resta es: {resultado:.2f}")
            elif opcion == 3:
                resultado = num1 * num2 
                print(f"La multiplicación es: {resultado:.2f}")
            elif opcion == 4:
                resultado = num1/num2
                print(f"La división es: {resultado:.2f}")
            else:
                print("La opción ingresa no es válida")
        except ValueError:
            print("Debes introducir un número válido.")

calculadora()