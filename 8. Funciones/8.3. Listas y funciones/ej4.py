""" Tu tarea es escribir y probar una función que toma un argumento (un año) y 
devuelve True si el año es un año bisiesto, o False si no lo es.

si el número del año no es divisible entre cuatro, es un año común.
de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
de lo contrario, si el número del año no es divisible entre 400, es un año común.
de lo contrario, es un año bisiesto.

La semilla de la función ya se muestra en el código esqueleto del editor.

Nota: también hemos preparado un breve código de prueba, que puedes utilizar 
para probar tu función.

El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. 
El código te dirá si alguno de tus resultados no es válido.

Ejemplo:
test_data = [1900, 2000, 2016, 1987]
expected = [False, True, True, False]

1900 → OK
2000 → OK
2016 → OK
1987 → OK
"""
def año_bisiesto(año):
    if año%4!=0:
        return False
    elif año%100!=0:
        return True
    elif año%400!=0:
        return False
    else:
        return True
año_prueba=[1900, 2000, 2016, 1987]
ToF_prueba=[False, True, True, False]

for i in range(len(año_prueba)):
    valor_año=año_bisiesto(año_prueba[i])
    if valor_año==ToF_prueba[i]:
        print(año_prueba[i]," Ok ")
    else:
        print(año_prueba[i]," Error ")
        