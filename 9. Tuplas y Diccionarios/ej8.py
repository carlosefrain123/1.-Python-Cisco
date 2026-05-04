""" Ejercicio 4: Registro de gastos del hogar
Un programa que:

Pide categorías de gastos y sus montos
Guarda todo en un diccionario
Al final muestra las categorías ordenadas con su gasto promedio """
diccionario={}
while True:
    cat_gastos=input("Ingrese la categoria de gastos: ")
    if cat_gastos=="":
        break
    monto=int(input("Ingrese los montos: "))
    if monto not in range(-1,1001):
        break
    if cat_gastos in diccionario:
        print("Categoria ya registrada")
        diccionario[cat_gastos]+=(monto,)
    else:
        print("Registrando...")
        diccionario[cat_gastos]=(monto,)
""" print(diccionario) """
for cat_gastos in diccionario:
    total=0
    conteo=0
    for monto in diccionario[cat_gastos]:
        total+=monto
        conteo+=1
    promedio=total/conteo
    print(cat_gastos,"->",promedio)