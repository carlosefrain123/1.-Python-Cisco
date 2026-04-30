""" Determinar si tres longitudes dadas pueden formar un triángulo. Para ello, la suma 
de cualquier par de lados debe ser mayor que el tercer lado. Si se cumple la condición, 
devolver True; en caso contrario, devolver False. """
def resultado(a,b,c):
    if a+b<c:
        return False
    if c+a<b:
        return False
    if b+c<a:
        return False
    else:
        return True
print(resultado(1, 1, 1))
print(resultado(1, 1, 3))
