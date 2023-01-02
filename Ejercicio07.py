def calcular_imc(peso, estatura):
    imc = peso / (estatura**2)
    return round(imc, 2)

peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
resultado = calcular_imc(peso, estatura)
print(f"Tu índice de masa corporal es {resultado}")
