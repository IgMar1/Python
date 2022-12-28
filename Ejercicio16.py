def convertir_fecha(fecha):
  # Separamos la fecha en día, mes y año
  dia, mes, anio = fecha.split("/")

  # Devolvemos la fecha en el formato aaaa/mm/dd
  return anio + "/" + mes + "/" + dia

# Define la fecha en el formato dd/mm/aaaa
fecha = "09/03/2022"

# Imprime la fecha en el formato aaaa/mm/dd
print(convertir_fecha(fecha)) # imprime 1973/12/04
