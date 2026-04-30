""" Solicitar al usuario las longitudes de tres lados y determinar si pueden formar 
un triángulo, verificando que la suma de cada par de lados sea mayor que el tercer lado.
Mostrar un mensaje indicando si es posible o no formar el triángulo """
def valor(a,b,c):
    return a+b>c and a+c>b and b+c>a

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

if valor(a,b,c):
    print("Tri+angulo")
else:
    print("No triángulo")