import pygame
from pygame.locals import *

#Cache dictionary
CACHE = {}

def load(surface, imageFile):
  """Return image from cache dictionary. If it does not exist, load it into cache."""
  
  global CACHE
  if not imageFile in CACHE: CACHE[imageFile] = pygame.image.load(imageFile).convert_alpha(surface)
  return CACHE[imageFile]


