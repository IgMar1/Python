def division_enteros(n, m):
  # Calcular el cociente y el resto de la división entera
  c = n // m
  r = n % m

  # Mostrar el resultado por pantalla
  print(f"{n} entre {m} da un cociente {c} y un resto {r}")

# Pedir al usuario que ingrese dos números enteros
n = int(input("Ingrese el primer número entero: "))
m = int(input("Ingrese el segundo número entero: "))

# Llamar a la función y pasarle los números ingresados por el usuario
division_enteros(n, m)
