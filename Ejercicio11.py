def ahorros(cantidad, interes):
  # Calcular la cantidad de ahorros después de 1, 2 y 3 años
  ahorros_1 = round(cantidad * (1 + interes / 100), 2)
  ahorros_2 = round(ahorros_1 * (1 + interes / 100), 2)
  ahorros_3 = round(ahorros_2 * (1 + interes / 100), 2)

  # Mostrar el resultado por pantalla
  print(f"La cantidad de ahorros después de 1 año es {ahorros_1}")
  print(f"La cantidad de ahorros después de 2 años es {ahorros_2}")
  print(f"La cantidad de ahorros después de 3 años es {ahorros_3}")

# Pedir al usuario que ingrese la cantidad depositada en la cuenta de ahorros y el interés anual
cantidad = float(input("Ingrese la cantidad depositada en la cuenta de ahorros: "))
interes = float(input("Ingrese el interés anual ofrecido por la cuenta: "))

# Llamar a la función y pasarle la cantidad y el interés ingresados por el usuario
ahorros(cantidad, interes)
