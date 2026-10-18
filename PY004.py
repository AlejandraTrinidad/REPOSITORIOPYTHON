# PY0004 Usando listas realiza las siguientes operaciones
# Parte de un menú base: ["Ensalada", "Sopa", "Pasta"].
# Haz una copia independiente llamada menu_hoy.
# Extiende menu_hoy con los especiales: ["Pescado", "Postre"].
# Retira el último plato añadido por error.
# Elimina “Sopa” si está.
# Escoge una posición del menú y eliminala.
# Muestra el menú al revés.
# Vacía por completo la lista base original y demuestra que menu_hoy no se ha visto afectada

lista = ["Ensalada", "Sopa", "Pasta"]
menu_hoy = lista.copy()

menu_hoy.extend(["Pescado", "Postre"])

menu_hoy.pop()

if "Sopa" in menu_hoy:
    menu_hoy.remove("Sopa")

menu_hoy.pop(1)

menu_hoy.reverse()

lista.clear()
print("Lista base (original):", lista)
print("Menú de hoy (copia):", menu_hoy)