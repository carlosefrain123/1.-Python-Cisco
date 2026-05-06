def validar_nota(nota):
    try:
        nota_valida=int(nota)
        if nota_valida<0 or nota_valida>20:
            raise ValueError
        return nota_valida 
    except ValueError:
        return "Error..."
print(validar_nota(20))
print(validar_nota("Hola"))
