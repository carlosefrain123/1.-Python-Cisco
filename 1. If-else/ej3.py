""" Como seguramente sabrás, debido a algunas razones astronómicas, el año puede ser bisiesto o común. 
Los primeros tienen una duración de 366 días, mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente regla para determinar el tipo de año:

si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.
Observa el código en el editor - solo lee un número de año y debe completarse con las instrucciones que implementan 
la prueba que acabamos de describir.


El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, según el valor ingresado. """

year=int(input("Ingrese un año: "))
while(year<=1582):
    print("Debe ser mayor al año 1582")
    year=int(input("Ingrese otro año: "))
if year&4!=0:
    print("Año común")
elif(year%100!=0):
    print("Año bisiesto.")
elif(year%400!=0):
    print("Año común.")
else:
    print("Año bisiesto")