# Entrada
cant = int(input("Por favor ingrese la cantidad:\n"))
print()
# Fin Entrada

# Variables
num = []

# Asignación de números y ordenarlos
for i in range(cant):
    num.append(int(input("Numero "+str(i+1)+":")))
# Se utiliza el metodo .append para poder
# Agregar los elementos digitados por el
# Usuario a la lista num y luego ordenarlos

# Fin Asignacion

# Ordenar Numeros
num.sort()
# Fin ordenar

# Salida

# Fin Salida
print("Numeros Ordenados: ")
for i in num:
    print(i, end=" ")
print()