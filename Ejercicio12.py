def coste_pan(barras):
  # Calcular el precio habitual de una barra de pan, el descuento por no ser fresca y el coste final total
  precio = 3.49
  descuento = 0.60
  coste = round(barras * precio * (1 - descuento), 2)

  # Mostrar el resultado por pantalla
  print(f"El precio habitual de una barra de pan es {precio}€")
  print(f"El descuento por no ser fresca es del {descuento * 100}%")
  print(f"El coste final total es de {coste}€")

# Pedir al usuario que ingrese el número de barras vendidas que no son del día
barras = int(input("Ingrese el número de barras vendidas que no son del día: "))

# Llamar a la función y pasarle el número de barras ingresado por el usuario
coste_pan(barras)
