productos = {"manzana": 0.40, "banana": 0.50, "cereza": 0.80}

claves = productos.keys()
print(claves)

valores = productos.values()
print(valores)

productos["naranja"] = 0.60
print(productos)

productos["banana"] = 0.75
print(productos)

print(productos.keys(), productos.values())
