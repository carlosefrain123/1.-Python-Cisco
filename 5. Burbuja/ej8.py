lista=[]
swapped=True
cantidad=int(input("Ingrese la cantidad de valores a colocar: "))

for i in range(cantidad):
    valores=int(input("Ingrese los valores correspondientes: "))
    lista.append(valores)

while swapped:
    swapped=False
    for i in range(len(lista)-1):
        if(lista[i]>lista[i+1]):
            lista[i],lista[i+1]=lista[i+1],lista[i]
print(lista)
print("El mayor es: ",max(lista))