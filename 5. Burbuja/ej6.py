lista=[]
condicion=True
cantidad=int(input("Ingrese la cantidad de valores: "))

for i in range(cantidad):
    valores=int(input("Ingrese los valores: "))
    lista.append(valores)
while condicion:
    condicion=False
    for i in range(len(lista)-1):
        if(lista[i]>lista[i+1]):
            condicion=True
            lista[i],lista[i+1]=lista[i+1],lista[i]
print(lista)