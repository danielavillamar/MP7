# MICROPROYECTO 7
# VIERNES 21 DE OCTUBRE DEL 2022
# Daniela Villamar 19086
# Walter Saldaña 19897
# Roberto Castillo 18546


# Importamos pygame 
import pygame
# Definición de pantalla del simulador
pixel_len = 12
height_pixels = 65
width_pixels = 60
width, height = width_pixels*pixel_len, height_pixels*pixel_len

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

ITERATIONS = 100
for _ in range(ITERATIONS):
  pygame.time.delay(10)
  pygame.display.flip()