inscritos_taller = {"Juan", "Marco", "David", "Polo"}

while True:
    respuesta = input("Introduce un nuevo nombre para añadir a los inscritos. Introduce 'fin' cuando quieras acabar: ")
    if respuesta.lower() == "fin":
        break
    elif not respuesta:
        print("La cadena está vacía")
        continue
    elif respuesta.startswith(" ") or respuesta.endswith(" "):
        print("El nombre no puede empezar ni terminar por espacios.\n")
        continue

    inscritos_taller.add(respuesta)

entrada_lotes = input("Introduce varios nombres separados por comas")
nuevos_lote = {nombre.strip() for nombre in entrada_lotes.split(",") if nombre.strip() != ""}
inscritos_taller.update(nuevos_lote)

copia_inscritos = inscritos_taller.copy()


nombre_baja = input("Introduce un nombre para dar de baja: ")
try:
    inscritos_taller.remove(nombre_baja)
    print(f"{nombre_baja} dado de baja correctamente")
except KeyError:
    print(f"{nombre_baja} no estaba en la lista, por lo que no se pudo dar de baja")

persona_buscar = input("\nIntroduce un nombre para comprobar si está inscrito: ")
if persona_buscar in inscritos_taller:
    print(f"Sí, '{persona_buscar}' está inscrito en el taller.")
else:
    print(f"No, '{persona_buscar}' no se encuentra en la lista.")

conjunto_personas = {"Jesus", "Lucía", "Marco", "Daniela"}
coincidencias = inscritos_taller.intersection(conjunto_personas)
if coincidencias:
    print(f"Hay personas del otro grupo inscritas: {coincidencias}")
else:
    print("Ninguna persona del otro grupo está inscrita.")

print(len(inscritos_taller))
print(sorted(inscritos_taller))