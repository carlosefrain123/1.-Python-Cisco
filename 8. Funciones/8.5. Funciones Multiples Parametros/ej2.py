""" Calcular el Índice de Masa Corporal (IMC) de una persona 
usando la fórmula IMC = peso (kg) / altura² (m), 
validando que el peso esté entre 20 y 200 kg y la 
altura entre 1.0 y 2.5 metros. Si los datos no son válidos, 
devolver None. """

""" def valor(peso,altura):
    if peso<20 or peso>200 or altura<1.0 or altura>2.5:
        return None
    IMC=peso/(altura)**2
    return IMC
peso=float(input("Ingrese el peso: "))
altura=float(input("Ingrese la altura: ")) """
""" formula(peso,altura) """
""" print("La formula es: ",valor(peso,altura)) """
    
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
