import copy

calificaciones = [
    {"alumno": "Ana", "modulo": "Programación", "nota": 7.5},
    {"alumno": "Ana", "modulo": "Sistemas", "nota": 8.0},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 6.0},
    {"alumno": "Ana", "modulo": "Programación", "nota": 9.0},
    {"alumno": "Luis", "modulo": "Programación", "nota": 5.5},
]

alumnos = {}
for c in calificaciones:
    alumnos.setdefault(c["alumno"], {}).setdefault(c["modulo"], []).append(c["nota"])

print(alumnos)

medias_alumnos = {}
for alumno, modulos in alumnos.items():
    maximas_modulos = [max(notas) for notas in modulos.values() if notas]
    if maximas_modulos:
        medias_alumnos[alumno] = sum(maximas_modulos) / len(maximas_modulos)

print("Media Aritmética")
print(medias_alumnos)


por_modulo = {}
for alumno, modulos in alumnos.items():
    for modulo, notas in modulos.items():
        if notas:
            por_modulo.setdefault(modulo, {})[alumno] = max(notas)

print("Estructura agrupada por módulo")
print(por_modulo)

aprobados_por_modulo = {
    modulo: {alumno: nota for alumno, nota in estudiantes.items() if nota >= 5}
    for modulo, estudiantes in por_modulo.items()
}

print("Aprobados por módulo")
print(aprobados_por_modulo)

correcciones = {'Ana': {'Programación': 0.75}}

alumnos_corregido = copy.deepcopy(alumnos)

for alumno, modulos_corr in correcciones.items():
    if alumno in alumnos_corregido:
        for modulo, ajuste in modulos_corr.items():
            lista_notas = alumnos_corregido.get(alumno, {}).get(modulo)
            if lista_notas:
                lista_notas[-1] += ajuste

print("Estructura tras aplicar correcciones a la última nota:")
print(alumnos_corregido)

def eliminar_matricula(estructura, alumno, modulo, indice):
    modulos_alumno = estructura.get(alumno)
    if not modulos_alumno:
        return None

    lista_notas = modulos_alumno.get(modulo)
    if not lista_notas:
        return None
    
    try:
        nota_eliminada = lista_notas.pop(indice)
    except IndexError:
        return None
    
    if not lista_notas:
        modulos_alumno.pop(modulo)
        
    if not modulos_alumno:
        estructura.pop(alumno)
        
    return nota_eliminada

nota_borrada = eliminar_matricula(alumnos, "Ana", "Programación", 0)
print(f"Nota eliminada: {nota_borrada}")
print("Estructura 'alumnos' tras la eliminación en cascada:")