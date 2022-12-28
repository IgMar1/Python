def contar_vocales(palabra):
  # Crear un diccionario con las vocales y sus contadores inicializados en 0
  vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

  # Iterar sobre cada letra de la palabra
  for letra in palabra:
    # Si la letra es una vocal, incrementar su contador en el diccionario
    if letra in vocales:
      vocales[letra] += 1

  # Devolver el diccionario de vocales
  return vocales

# Llamar a la función y guardar el resultado en una variable
resultado = contar_vocales("paragaricutirimicuaro")

# Imprimir el resultado
print(resultado)
