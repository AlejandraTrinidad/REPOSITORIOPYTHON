palabras = ["python", "java   ", "javascript", "go", "rust", "", ""]


diccionario = {palabra.strip() : len(palabra.strip()) for palabra in palabras}
print(diccionario)

diccionario2 = {palabra.strip() : len(palabra.strip()) for palabra in palabras if palabra.strip() != ""}
print(diccionario2)

diccionario3 = {
    (palabra.strip().upper() if len(palabra.strip()) > 5 else palabra.strip().lower()): 
    
    len(palabra.strip()) 
    
    for palabra in palabras 
    
    if palabra.strip() != ""
}

print(diccionario3)