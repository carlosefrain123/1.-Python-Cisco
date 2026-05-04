"""  Verificar antes de eliminar """
agenda = {"Bob": 123, "Andy": 456, "María": 789}
if "Andy" in agenda:
    del agenda["Andy"]
    print(agenda)
else:
    print("No existe Andy")