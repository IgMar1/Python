def peso_paquete(payasos, munecas):
  # Calcular el peso total del paquete
  peso = payasos * 112 + munecas * 75

  # Mostrar el resultado por pantalla
  print(f"El peso total del paquete es {peso} g")

# Pedir al usuario que ingrese el número de payasos y muñecas en el paquete
payasos = int(input("Ingrese el número de payasos en el paquete: "))
munecas = int(input("Ingrese el número de muñecas en el paquete: "))

# Llamar a la función y pasarle el número de payasos y muñecas ingresados por el usuario
peso_paquete(payasos, munecas)
