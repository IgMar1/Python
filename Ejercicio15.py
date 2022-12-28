def es_divisible_por_dos(numeros):
  # Inicializamos una lista vacía para almacenar los números divisibles por 2
  divisibles_por_dos = []

  # Iteramos sobre cada número en la lista de números
  for numero in numeros:
    # Si el número es divisible por 2, lo agregamos a la lista de números divisibles por 2
    if numero % 2 == 0:
      divisibles_por_dos.append(numero)

  # Devolvemos la lista de números divisibles por 2
  return divisibles_por_dos

# Define la lista de números
numeros = [1, 2, 3, 4, 5]

# Imprime la lista de números divisibles por 2
print(es_divisible_por_dos(numeros)) # imprime [2, 4]
