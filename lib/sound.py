import pygame

CHANNEL = [0]
SOUNDS = {}
MUSIC = {}

def init():
  """Initilize the noise engine"""
  
  #Initlize python engine
  pygame.mixer.init()
  global SOUNDS, MUSIC
  
  #Load sound objects
  SOUNDS['bounce'] = pygame.mixer.Sound('content/sounds/bounce.wav')
  SOUNDS['break'] = pygame.mixer.Sound('content/sounds/break.wav')
  SOUNDS['miss'] = pygame.mixer.Sound('content/sounds/miss.wav')
  
  #Load music objects
  CHANNEL[0] = pygame.mixer.Channel(0)
  CHANNEL[0].set_volume(0.1)

def play(name):
  """Play a sound/music object"""
  
  if name in SOUNDS.keys():
    CHANNEL[0].play(SOUNDS[name])

  elif name in MUSIC.keys():
    pygame.mixer.music.load(MUSIC[name])
    pygame.mixer.music.play()

init()
