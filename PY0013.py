import time

def sustituirCaracter():
    try:
        frase = input("Introduce una frase: ")
        caracter_sustituir = input("Introduce el carácter a sustituir:\t")
        caracter_nuevo = input("Introduce el nuevo carácter:\t")
        if len(caracter_sustituir) != 1 or len(caracter_nuevo) != 1:
            print("Solo queríamos un caracter")
            time.sleep(3)
            return
        frase_modificada = frase.replace(caracter_sustituir, caracter_nuevo)
        print("Frase resultante:", frase_modificada)

        frase_dos_primeras = frase.replace(caracter_sustituir, caracter_nuevo, 2)
        print("Cambiando solo las 2 primeras:", frase_dos_primeras)
    except Exception as error:
        print("Ocurrió un error inesperado")


sustituirCaracter()