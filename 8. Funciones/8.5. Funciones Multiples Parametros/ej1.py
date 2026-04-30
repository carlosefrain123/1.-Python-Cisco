""" Halla IMC= peso en Kg/ (Altura en metros)**2 """
def formula(peso,altura):
    IMC=peso/(altura)**2
    """ print("El IMC es: ",IMC) """
    return IMC
peso=float(input("Ingrese el peso: "))
altura=float(input("Ingrese la altura: "))
""" formula(peso,altura) """
print("La formula es: ",formula(peso,altura))