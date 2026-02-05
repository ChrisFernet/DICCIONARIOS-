# diccionario vacio
dicc = {}
dicc = dict()

# asignar valores
camper = {
    "nombre":"Sebastian",
    "edad":"18",
    "carrera":"Ing. en sistemas"}

# creación con dict

producto = dict(nombre = "Portatil", precio =  4000_000, stock = 10)

# creación con lista de tuplas 

pares = [("a", 1), ("b", 2), ("c", 3)]
diccionario = dict(pares)

# acceso

print(camper["nombre"])
print(camper.get("edad"))
print(camper.get("pasatiempos", "ping pong"))

# metodo keys(): devuelve lista con todas las llaves

print(camper.keys())
camper["pasatiempos"] = "futbol"

# metodo values(): devuelve todos los valores

print(camper.values())

# metodo items(): devuelve todos los pares clave-valor como una lista de tuplas

print(camper.items())

# recorrer:
# 1. con keys()

for key in camper.keys():
    print(f"camper [{key}] -> {camper[key]}", end=", ")

# 2. con items()

for llave, valor in camper.items():
    print(f"camper[{llave}] -> {valor}", end = ", ")

# pop(): elimina una clave y retorna su valor 

print(camper.pop("pasatiempos"))
print(camper)

# popitem(): elimina y retorna el ultimo par clave-valor insertado

print(camper.popitem())
print(camper)

# clear(): elimina todos los elementos del diccionario
# camp.clear()
# camper = {}

# copy(): crea una copia del diccionario
camper_bak = {}
camper_bak = camper.copy()
print(camper_bak)

# setdefault(): retorna el valor de una clave.
# si no existe, la crea con un valor por defecto

print(camper.setdefault("pasatiempo", ["furbo", "programar", "parrandear"]))
print(camper)
print(camper.setdefault("pasatiempo", "dormir"))

# len(): cantidad de pares-valor que hay en el diccionario

print(len(camper))

# in: verifica si existe una llave en el diccionario

print("sexo" in camper)

# del: elimina una llave

del camper["pasatiempo"]

# any():  verifica si al menos un valor de las llaves verdadero

camper["sueldo"] = 0
print(camper)
print(any(camper.values())) # -> true

# all(: verifica si todos los valores de las llaves son verdaderos
print(all(camper.values())) # -> false