def lista(valores):
    try:
        promedio=sum(valores)/len(valores)
        return promedio
    except ZeroDivisionError:
        return "Error"
print(lista([10,20,30]))
print(lista([]))
