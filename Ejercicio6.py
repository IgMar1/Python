def suma_enteros(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

numero = int(input("Introduce un entero positivo: "))
resultado = suma_enteros(numero)
print(f"La suma de los enteros desde 1 hasta {numero} es {resultado}")