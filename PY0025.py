# PY0025. Crear un programa de consola que maneje una lista de países con los siguientes requisitos.
# Imprimir un menú como el siguiente.
#     "MENÚ. Elija una de las siguientes opciones marcando su número:"
#     "1. Imprimir alfabéticamente en orden ascendente"
#     "2. Imprimir alfabéticamente en orden descendente"
#     "3. Añadir País"
#     "4. Eliminar Pais"
#     "5. Salir"

# Se empezará con la lista ”España, Argentina, Perú”. Esta lista no podrá contener más de 6 países.
# Pedir al usuario que elija una opción de menú hasta que pulse la opción de salir. Ha de controlarse que se ha introducido un entero con el número de la opción y 
# que el número está entre el 1 y el 5. En caso de no cumplirse algo, se le indicará al usuario y se le mostrará el menú nuevamente.
# Se debe contabilizar el número de ejecuciones del menú y mostrarlo por consola después de cada ejecución. Se debe mostrar aunque haya alguna excepción o se haya elegido 
# la opción de salir. (ver bloque try)
# Después de cada ejecución, se mostrará una línea con setenta # repetidas, para diferenciar con la siguiente ejecución, y terminará en dos saltos de línea. 
# Además, solo se mostrará si la ejecución ha ido bien y si no se ha elegido la opción salir.
# Cuando finalice el programa completamente, si todo ha ido bien, se le dará las gracias al usuario, se le indicará el número total de intentos y se le mandará un saludo.
# Después de mostrar la lista de países, se pondrán dos saltos de línea. 
# Para añadir y borrar:
# Los países, independientemente de cómo los escriba el usuario, se añadirán con la primera letra en mayúsculas y las demás en minúsculas.
#  A la hora de borrarlos también se tendrá esto en cuenta y también dará igual cómo lo escriba. 
# No se puede añadir un país nulo “”.
# Después de añadir o borrar, se le confirmará al usuario que se ha realizado la operación y se le mostrará la lista de países.
# Hay que tener en cuenta el tamaño de la lista.
# Hay que tener en cuenta si el país indicado se encuentra en la lista. No se admitirán países repetidos, ni se puede borrar uno que no esté 


lista_paises = ["España", "Argentina", "Perú"]
limite = 6
total_ejecuciones = 0

while True:
    try:
        print("MENÚ. Elija una de las siguientes opciones marcando su número: ")
        print("1. Imprimir alfabéticamente en orden ascendente ")
        print("2. Imprimir alfabéticamente en orden descendente ")
        print("3. Añadir País ")
        print("4. Eliminar Pais ")
        print("5. Salir ")

        respuesta = int(input("Elija una opción: "))

        if respuesta < 1 or respuesta > 5:
            print("Error: Debe ingresar un número entero entre 1 y 5.\n")
            continue

        opcion_salir = False
        operacion_correcta = True

        if respuesta == 1:
            print(sorted(lista_paises))
            print("\n")

        elif respuesta == 2:
            print(sorted(lista_paises, reverse=True))
            print("\n")

        elif respuesta == 3:
            if len(lista_paises) >= limite:
                print(f"Error: La lista ya ha alcanzado el límite máximo de {limite} países.")
            else:
                nuevo_pais = input("Dime el nombre del país que quieres añadir: ").strip().capitalize()
                
                if nuevo_pais == "":
                    print("Error: No se puede añadir un país nulo/vacío.")
                elif nuevo_pais in lista_paises:
                    print(f'Error: El país "{nuevo_pais}" ya se encuentra en la lista (no se admiten repetidos).')
                else:
                    lista_paises.append(nuevo_pais)
                    print(f'Confirmación: Se ha añadido "{nuevo_pais}" correctamente.')
                    print("Lista de países actual:", lista_paises)
                    print("\n")

        elif respuesta == 4:
            pais_eliminar = input("Dime el nombre del país que quieres eliminar: ").strip().capitalize()
            
            if pais_eliminar not in lista_paises:
                print(f'Error: El país "{pais_eliminar}" no está en la lista.')
            else:
                lista_paises.remove(pais_eliminar)
                print(f'Confirmación: Se ha eliminado "{pais_eliminar}" correctamente.')
                print("Lista de países actual:", lista_paises)
                print("\n")

        elif respuesta == 5:
            opcion_salir = True
            break
    except ValueError:
        print("Debe ingresar un número entero válido.\n")
    finally:
        total_ejecuciones += 1
        print(f"Número de ejecuciones del menú: {total_ejecuciones}")

        try:
            if 'operacion_correcta' in locals() and operacion_correcta and not opcion_salir:
                print("#" * 70)
                print("\n")
        except NameError:
            pass

print("\nMuchas gracias por utilizar el programa!")
print(f"Número total de intentos: {total_ejecuciones}")
print("Un saludo")