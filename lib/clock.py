import pygame
from pygame.locals import *

#Initilize global clock
CLOCK = pygame.time.Clock()

def tick(fps=60):
  CLOCK.tick(fps)
