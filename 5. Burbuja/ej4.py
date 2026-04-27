lista=[]
swapped=True
num=int(input("Ingrese cuantos valores desea ingresar: "))

for i in range(num):
    valor=int(input("Ingrese valores:"))
    lista.append(valor)

while swapped:
    swapped=False
    for i in range(len(lista)-1):
        if(lista[i]>lista[i+1]):
            swapped=True
            lista[i],lista[i+1]=lista[i+1],lista[i]
print("Lista completa: "+str(lista))
