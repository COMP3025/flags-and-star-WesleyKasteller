import sys

import pygame as pg
from pygame.locals import QUIT
import math

def draw_star(screen, position, size, angle):
  x, y = position
  ang_rad = math.radians(angle)
  ang = math.radians(36)

  points = []
  for _ in range(5):
    inx = x + size * math.cos(ang_rad)
    iny = y - size * math.sin(ang_rad)
    points.append((inx, iny))

    ang_rad += ang

    outx = x + size * 0.4 * math.cos(ang_rad)
    outy = y - size * 0.4 * math.sin(ang_rad)
    points.append((outx, outy))

    ang_rad += ang

  pg.draw.polygon(screen, (255, 255, 255), points)


pg.init()
DISPLAYSURF = pg.display.set_mode((400, 300))
pg.draw.rect(DISPLAYSURF, (255, 255, 255), pg.Rect(100, 100, 200, 100))
pg.draw.rect(DISPLAYSURF, (0, 0, 255), pg.Rect(100, 100, 200, 20))
pg.draw.rect(DISPLAYSURF, (0, 0, 255), pg.Rect(100, 140, 200, 20))
pg.draw.rect(DISPLAYSURF, (0, 0, 255), pg.Rect(100, 180, 200, 20))
pg.draw.polygon(DISPLAYSURF, (255, 0, 0), ((100, 100), (175, 150), (100, 200)))
draw_star(DISPLAYSURF, (130, 150), 14, 17)
while True:
  for event in pg.event.get():
    if event.type == QUIT:
      pg.quit()
      sys.exit()
  pg.display.update()
