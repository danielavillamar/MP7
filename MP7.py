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


class FuzzyDistance:
  """Logica difusa

  Variables a considerar:
  - Distancia [0, 700]
  - Direccion [0, 359]

  Variables linguisticas de entrada:
  - Distancia:
    - 0. Estoy en el punto
    - 1. Estoy cerca
    - 2. Estoy lejos
  - Direccion:
    - 0. Me dirijo hacia el objetivo
    - 1. Me dirijo a la derecha del objetivo
    - 2. Me dirijo a la izquierda del objetivo
    - 3. Estoy en direccion opuesta
  
  Variables linguisticas de salida:
  - 0. Patear el balon
  - 1. Correr a la izquierda
  - 2. Correr a la derecha
  - 3. Correr recto
  - 4. Dar la vuelta

  Cláusulas de Horn:
  - Si estoy en el punto y Me dirijo hacia el objetivo => Patear el balon
  - Si estoy cerca o lejos y Me dirijo a la derecha del objetivo => Correr a la izquierda
  - Si estoy cerca o lejos y Me dirijo a la izquierda del objetivo => Correr a la derecha
  - Si estoy cerca o lejos y Me dirijo hacia el objetivo => Correr recto
  - Si estoy cerca o lejos y Estoy en direccion opuesta  => Dar la vuelta
  """
  point = 12
  close = 36
  far = 500

  straight = 90
  right = 45
  left = 135
  opposite = 270


  @classmethod
  def get_fuzzy_distance(cls, distance):
    fuzzy_distance = [
      distance / cls.point,
      distance / cls.close,
      distance / cls.far
    ]
    return fuzzy_distance.index(max(fuzzy_distance))

  @classmethod
  def get_fuzzy_rotation(cls, angle):
    fuzzy_rotation = [
      angle / cls.straight,
      angle / cls.right,
      angle / cls.left,
      angle / cls.opposite
    ]
    return fuzzy_rotation.index(max(fuzzy_rotation))

  @classmethod
  def horn(cls, fd, fr):
    if (fd == 0) and (fr == 0):
      return 0
    elif (fd == 1 or fd == 2) and (fr == 1):
      return 1
    elif (fd == 1 or fd == 2) and (fr == 2):
      return 2
    elif (fd == 1 or fd == 2) and (fr == 0):
      return 3
    else:
      return 4


class Simulation(object):
  def __init__(self, screen, initial=None):
    self.screen = screen
    self.modx = width 
    self.mody = height

    # Coordenadas del jugador
    self.player_x = random.randint(24, 700)
    self.player_y = random.randint(24, 700)

    # Stats del jugador
    self.player_width = 20
    self.player_height = 30
    self.player_current_direction = (0,0)

    # Coordenadas de la pelota
    self.ball_x = random.randint(24, 700)
    self.ball_y = random.randint(24, 700)

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
    ...

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



run = True
while(run):
  pygame.time.delay(10)
  pygame.display.flip()
  simulation.moveUp(0, 0)

  for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
    if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
      run = False
