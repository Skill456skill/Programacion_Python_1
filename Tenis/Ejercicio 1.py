# Inicio del Juego
print("\nEmpecemos!!")

# Variables
A = [0] * 5
B = [0] * 5
# Fin variables

# Entradas A y B
for i in range(5):
    A[i] = int(input("Número de juegos ganados por A en el Set " + str(i + 1) + ": "))
    B[i] = int(input("Número de juegos ganados por B en el Set " + str(i + 1) + ": "))
    print()

# Fin Entradas A y B

# Inicio Bucle
for i in range(5):
    print("\n--- Set" + str(i + 1) + " ---")
    print(" Juegos Ganados")
    print("  A: " + str(A[i]) +"    B: " + str(B[i]))

    # Conteo de Sets
    if A[i] - 2 == B[i]:
        print("    Ganador: A")
    elif B[i] - 2 == A[i]:
        print("    Ganador: B")
    elif A[i] - 1 == B[i] or B[i] - 1 == A[i] or A[i] == B[i]:
        print("Aún no termina, Empate a 7")
    elif B[i] == 7 and A[i] != 6 or A[i] == 7 and B[i] != 6 or A[i] > 7 or B[i] > 7:
        print("    Inválido")
    # Fin Conteo

# Fin Bucle
# Fin Juego