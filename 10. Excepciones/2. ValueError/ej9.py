def suma(a,b):
    try:
        vA=int(a)
        vb=int(b)
        suma=vA+vb
        return(suma)
    except:
        return "Los dos valores tienen que ser números"
print(suma(20,40))
print(suma(20,"a"))
