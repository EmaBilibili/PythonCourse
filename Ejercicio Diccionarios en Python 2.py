edades = {"Juan": 28, "Elena": 32, "Marcos": 17}
print(f"Diccionario original: {edades}")

print(f"La edad de Elena es: {edades['Elena']}")

edades["Juan"] = 29
print(f"La edad de Juan ha sido modificada a: {edades['Juan']}")

edades["Luisa"] = 25

print(f"Diccionario final actualizado: {edades}")