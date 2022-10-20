# MICROPROYECTO 7
# VIERNES 21 DE OCTUBRE DEL 2022
# Daniela Villamar 19086
# Walter Saldaña 19897
# Roberto Castillo 18546


# Importamos pygame 
import pygame
import random
# Definición de pantalla del simulador
pixel_len = 12
height_pixels = 65
width_pixels = 60
width, height = width_pixels*pixel_len, height_pixels*pixel_len

# Colres del jugador y la pelota
player_color = (0,0,0) # Black
ball_color = (0, 0, 0) # Black



# Creación de la cancha
def createHorizontalLine(xo, xf, y):
  return [(x, y) for x in range(xo, xf)]

def createVerticalLine(yo, yf, x):
  return [(x, y) for y in range(yo, yf)]

class Simulation(object):
  def __init__(self, screen, initial=None):
    self.screen = screen
    self.modx = width 
    self.mody = height

    # Coordenadas del jugador
    self.player_x = 30
    self.player_y = 30

    # Stats del jugador
    self.player_width = 20
    self.player_height = 30
    self.player_current_direction = (0,0)

    # Coordenadas de la pelota
    self.ball_x = 100
    self.ball_y = 100

    # Stats de la pelota
    self.ball_width = 10
    self.ball_velocity = 20
    self.ball = pygame.draw.circle(screen, ball_color, (self.ball_x, self.ball_y), self.ball_width)
    self.player = pygame.draw.rect(screen, player_color, (self.player_x, self.player_y, self.player_width, self.player_height))

    for point in initial:
      self.paint(point[0], point[1])

  def paint(self, x, y, color=(255, 255, 255)):
    px = x*pixel_len
    py = y*pixel_len

    for i in range(px, px+pixel_len):
      for j in range(py, py+pixel_len):
        self.screen.set_at((i, j), color)

  def moveUp(self, x, y):
    pass
  
  def moveUp(self, x, y):
    pass
  
  def moveUp(self, x, y):
    pass
  
  def moveUp(self, x, y):
    pass

  # La dirección tiene que ser un vector unitario
  def ball_interactions(self, direction, strength): 
    direction_x = direction[0]
    direction_y = direction[1]

    # derecha
    if direction_x == 1: 
      if self.ball_x + strength > self.win_width:
        self.ball_interactions((-direction_x, 0), strength) 
      else:
        self.ball_x += strength

    # izquierda
    if direction_x == -1:  
      if self.ball_x - strength < 0:
        self.ball_interactions((-direction_x, 0), strength) 
      else:
        self.ball_x -= strength
    
    # abajo
    if direction_y == 1:
      if self.ball_y + strength > self.win_height:
        self.ball_interactions((0, -direction_y), strength) 
      else:
        self.ball_y += strength
    
    # arriba
    if direction_y == -1:  
      if self.ball_y - strength < 0:
        self.ball_interactions((0, -direction_y), strength) 
      else:
        self.ball_y -= strength

  # Funcion para detectar colisiones
  def collisions(self):
    if self.ball.colliderect(self.player):
      self.playerInteraction()

  # Interacción con el jugador
  def playerInteraction(self):
    self.ball_interactions(self.player_current_direction, self.ball_velocity * 2) 

# START
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((35, 192, 56))
pygame.display.flip()

lines = []

lines.extend(createHorizontalLine(0, 20, 10))
lines.extend(createVerticalLine(10, height_pixels-9, 20))
lines.extend(createHorizontalLine(0, 20, height_pixels-10))

lines.extend(createVerticalLine(30, 38, 0))
lines.extend(createVerticalLine(30, 38, 1))

simulation = Simulation(
  screen,
  initial=lines,
)



ITERATIONS = 1000
for _ in range(ITERATIONS):
  pygame.time.delay(10)
  pygame.display.flip()