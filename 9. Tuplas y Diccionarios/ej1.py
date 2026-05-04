""" agenda = {}

1) update → agregar personas con sus notas correspondientes

2) keys → ver nombres

3) items → ver todo

4) sorted → ordenar

5) del → eliminar """

agenda={}

agenda.update({"Efrain":20,"Brenda":18})
print("1) Agregar personas")
print(agenda)
print("2) Keys")
for i in agenda.keys():
    print(i,"->",agenda[i])
print("3) items")
for el1,el2 in agenda.items():
    print(el1,"->",el2)
print("4) sorted")
for i in sorted(agenda.keys()):
    print(i,"->",agenda[i])
print("5) del")
del agenda["Efrain"]
print(agenda)
