import pygame, os
from pygame.locals import *
from lib import img


#Globals
SURFACE = None
RESOLUTION = None
TITLE = None
ICONFILE = os.path.join('content','images','ball.png')


def init(r, t):
  """Initilize the display"""

  #Write inputs into the global variables
  global SURFACE, RESOLUTION, TITLE
  RESOLUTION = r
  TITLE = t
  
  #Initlize pygame library
  os.environ["SDL_VIDEO_CENTERED"] = "1"
  pygame.init()

  #Set title and icon
  icon = pygame.image.load(ICONFILE)
  pygame.display.set_caption(TITLE)
  pygame.display.set_icon(icon)

  #Open a new display
  SURFACE = pygame.display.set_mode((RESOLUTION[0],RESOLUTION[1]),0,32)

  #Return the new display
  return SURFACE
  
def update():
  pygame.display.update()
  
