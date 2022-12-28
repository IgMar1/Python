def calcular_paga():
  # Pedimos al usuario que introduzca el número de horas trabajadas
  horas_trabajadas = input("Por favor, introduce el número de horas trabajadas: ")
  
  # Convertimos el valor introducido a un número entero
  horas_trabajadas = int(horas_trabajadas)
  
  # Pedimos al usuario que introduzca el coste por hora
  coste_por_hora = input("Por favor, introduce el coste por hora: ")
  
  # Convertimos el valor introducido a un número entero
  coste_por_hora = int(coste_por_hora)
  
  # Calculamos la paga
  paga = horas_trabajadas * coste_por_hora
  
  # Mostramos la paga por pantalla
  print("La paga es: " + str(paga))

# Llamamos a la función calcular_paga
calcular_paga()