lista=[]
swapped=True
cantidad=int(input("Ingrese la cantidad de números a insertar: "))

for i in range(cantidad):
    valores=int(input("Ingrese los valores: "))
    lista.append(valores)
    
while swapped:
    swapped=False
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            swapped=True
            lista[i],lista[i+1]=lista[i+1],lista[i]
print("Lista completa: "+str(lista))