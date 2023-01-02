# Incluimos las librerias necesarias
import pygame
import random
import sys

# Inicializamos Pygame
pygame.init()

# Definimos algunas variables
ANCHO = 400
ALTO = 600
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
VELOCIDAD = 100
TAMANO_CELDA = 20

# Creamos la ventana del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")

# Creamos los botones de inicio y cierre
boton_inicio = pygame.Rect(10, 550, 60, 20)
boton_cierre = pygame.Rect(75, 550, 60, 20)

# Definimos la variable "juego_iniciado" y la lista "serpiente"
juego_iniciado = False
serpiente = []

# Bucle principal del juego
while True:
    # Procesamos los eventos del juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Comprobamos si se ha pulsado el botón de inicio
            if boton_inicio.collidepoint(evento.pos):
                # Iniciamos el juego
                serpiente = [(ANCHO // 2, ALTO // 2)]
                comida = (random.randint(0, ANCHO // TAMANO_CELDA - 1) * TAMANO_CELDA, 
                          random.randint(0, ALTO // TAMANO_CELDA - 1) * TAMANO_CELDA)
                direccion = "ARRIBA"
                juego_iniciado = True
            # Comprobamos si se ha pulsado el botón de cierre
            elif boton_cierre.collidepoint(evento.pos):
                # Cerramos el juego
                pygame.quit()
                sys.exit()
        elif juego_iniciado and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != "ABAJO":
                direccion = "ARRIBA"
            elif evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                direccion = "ABAJO"
            elif evento.key == pygame.K_LEFT and direccion != "DERECHA":
                direccion = "IZQUIERDA"
            elif evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                direccion = "DERECHA"

    # Actualizamos la posición de la serpiente
    if juego_iniciado:
        x, y = serpiente[0]
        if direccion == "ARRIBA":
            y -= TAMANO_CELDA
        elif direccion == "ABAJO":
            y += TAMANO_CELDA
        elif direccion == "IZQUIERDA":
            x -= TAMANO_CELDA
        elif direccion == "DERECHA":
            x += TAMANO_CELDA
        serpiente.insert(0, (x, y))

    # Comprobamos si la serpiente ha comido la comida
        if serpiente[0] == comida:
            comida = (random.randint(0, ANCHO // TAMANO_CELDA - 1) * TAMANO_CELDA, 
                      random.randint(0, ALTO // TAMANO_CELDA - 1) * TAMANO_CELDA)
        else:
            serpiente.pop()

        # Comprobamos si la serpiente ha chocado contra una pared o se ha mordido a sí misma
        if x < 0 or y < 0 or x >= ANCHO or y >= ALTO or (x, y) in serpiente[1:]:
            juego_iniciado = False

    # Dibujamos el juego
    ventana.fill(NEGRO)
    
    # Dibujamos el botón de inicio
    pygame.draw.rect(ventana, BLANCO, boton_inicio)
    texto = pygame.font.Font(None, 15).render("Iniciar", True, NEGRO)
    x = 10 + 30 - texto.get_width() // 2
    y = 550 + 50 - texto.get_height() // 0.22
    ventana.blit(texto, (x, y))

    # Dibujamos el botón de inicio
    pygame.draw.rect(ventana, BLANCO, boton_cierre)
    texto = pygame.font.Font(None, 15).render("Cerrar", True, NEGRO)
    x = 75 + 30 - texto.get_width() // 2
    y = 550 + 50 - texto.get_height() // 0.22
    ventana.blit(texto, (x, y))


    # Si el juego ha sido iniciado, dibujamos la serpiente y la comida
    if juego_iniciado:
        for x, y in serpiente:
            pygame.draw.rect(ventana, VERDE, pygame.Rect(x, y, TAMANO_CELDA, TAMANO_CELDA))
        pygame.draw.rect(ventana, ROJO, pygame.Rect(comida[0], comida[1], TAMANO_CELDA, TAMANO_CELDA))

    # Actualizamos la pantalla
    pygame.display.update()

    # Esperamos un poco antes de volver a iterar
    pygame.time.delay(VELOCIDAD)