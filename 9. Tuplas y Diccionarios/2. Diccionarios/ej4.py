hijos={"Efrain":23,"Brenda":19}
nombre=["Efrain","Carlos","Anahí","Brenda"]

""" for i in hijos:
    if i in nombre:
        print(i,"Si están")
    else:
        print("No estan") """

for i in nombre:
    """ print(i) """
    if i in hijos:
        print(i," Si está")
    else:
        print("No está")
    