"""
El usuario ingresa N leetras y el
programa debe contar las cantidad de veces 
que aparece una vocal en esas letras ingresadas

"""

n = int(input("cantidad de letras a ingresar?: "))
vocales = {"a":0, "e":0, "i":0, "o":0, "u":0}

for i in range(n):
    letra = input(f"letra {i+1}: ").strip()
    if letra in vocales:
        vocales[letra] += 1

for k, v in vocales.items():
    print(f"Cantidad de {k} es {v}")