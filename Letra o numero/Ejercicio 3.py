# Variables
caracter1 = ""
caracter2 = ""
caracter3 = ""
caracter4 = ""
# Fin Var

# Entrada
print("Por favor ingrese un caracter:")
entrada = input()
# Fin entrd

# Bucle y Condicional
for i in range(len(entrada)):
    ascii_value = ord(entrada[i])

    # Numeros
    if 48 <= ascii_value <= 57:
        caracter1 += entrada[i]
    # Mayusculas
    if 65 <= ascii_value <= 90:
        caracter2 += entrada[i]
    # Minusculas
    if 97 <= ascii_value <= 122:
        caracter3 += entrada[i]
    # Caracteres especiales
    if (32 <= ascii_value <= 47) or (58 <= ascii_value <= 64) or (91 <= ascii_value <= 96) or (123 <= ascii_value <= 127):
        caracter4 += entrada[i]

# Fin Bucle y Cond

# Salida
print("Caracter 1:", caracter1)
print("Caracter 2:", caracter2)
print("Caracter 3:", caracter3)
print("Caracter 4:", caracter4)
# Fin sald