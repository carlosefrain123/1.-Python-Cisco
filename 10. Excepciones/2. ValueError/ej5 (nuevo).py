def validar_nota(nota):
    try:
        cNota=int(nota) 
        if cNota<0 or cNota>20:
            raise ValueError
        return cNota
    except ValueError:
        return "Error en convertir en número"
print(validar_nota("15"))    # 15
print(validar_nota("hola"))  # Error: nota inválida
print(validar_nota("25"))    # Error: nota inválida
    