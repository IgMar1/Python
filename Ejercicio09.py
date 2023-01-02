def inversion(cantidad, interes, anios):
  # Calcular el capital obtenido en la inversión
  capital = cantidad * (1 + interes / 100) ** anios

  # Mostrar el resultado por pantalla
  print(f"El capital obtenido en la inversión es {capital}")
  
# Pedir al usuario que ingrese la cantidad a invertir, el interés anual y el número de años
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual: "))
anios = int(input("Ingrese el número de años: "))

# Llamar a la función y pasarle los valores ingresados por el usuario
inversion(cantidad, interes, anios)
