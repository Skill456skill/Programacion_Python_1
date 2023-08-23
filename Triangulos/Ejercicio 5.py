print("\nNota: Para numeros decimales usar '.'\n")
print("Por favor ingrese el lado a")
a = float(input())
print("Por favor ingrese el lado b")
b = float(input())
print("Por favor ingrese el lado c")
c = float(input())

if a + b > c and b + c > a and a + c > b:
    if a == b and b == c:
        print("Triángulo equilátero")
    elif a == b or b == c or a == c:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")
else:
    print("Triángulo inválido")