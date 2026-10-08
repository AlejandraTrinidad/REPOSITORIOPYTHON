cadena = input("Ingresa una frase: ").lower()
letras_contadas = []
for caracter in cadena:
    if caracter == " ":
        continue
    if caracter not in letras_contadas:
        cantidad = cadena.count(caracter)
        print(f"El carácter '{caracter}' aparece {cantidad} veces.")
        letras_contadas.append(caracter)