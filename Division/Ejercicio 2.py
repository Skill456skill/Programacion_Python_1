print()
print("Por favor Ingrese el numero dividendo: ")
a = float(input())
print("Por favor Ingrese el numero divisor: ")
b = float(input())
print("------------------------------------")

# Division
if b == 0:
    print("Error!!!")
    print("No se puede dividir entre cero")
elif a % b == 0:
    print("La division es exacta")
    print("Cociente:", a / b)
    print("Residuo:", a % b)
else:
    print("La division no es exacta")
    print("Cociente:", a / b)
    print("Residuo:", a % b)
print()
# Fin Division