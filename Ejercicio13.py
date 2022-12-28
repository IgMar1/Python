def factorial(numero):
  # Inicializar el resultado en 1
  resultado = 1

  # Calcular el factorial del número
  for i in range(1, numero+1):
    resultado *= i

  # Devolver el resultado
  return resultado

# Llamar a la función y guardar el resultado en una variable
resultado = factorial(4)

# Imprimir el resultado
print("El factorial de 4 es " + str(resultado))
