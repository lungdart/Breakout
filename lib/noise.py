import pygame, os

CHANNEL = [0]
LEVELS = [.65,0.55]
MUSIC = {}
SOUNDS = {}

def init():
  """Initilize the noise engine"""
  
  #Initlize python engine
  pygame.mixer.init()
  global SOUNDS, MUSIC
  
  #Load sound objects
  SOUNDS['bounce'] = pygame.mixer.Sound(os.path.join('content','sounds','bounce.wav'))
  SOUNDS['break'] = pygame.mixer.Sound(os.path.join('content','sounds','break.wav'))
  SOUNDS['miss'] = pygame.mixer.Sound(os.path.join('content','sounds','miss.wav'))
  CHANNEL[0] = pygame.mixer.Channel(0)
  CHANNEL[0].set_volume(LEVELS[1])
  
  #Load music objects
  MUSIC['menu'] = os.path.join('content','sounds','menu.mp3')
  MUSIC['level'] = os.path.join('content','sounds','level1.mp3')
  MUSIC['gameover'] = os.path.join('content','sounds','gameover.mp3')

def play(name):
  """Play a sound/music object"""
  
  if name in SOUNDS.keys():
    CHANNEL[0].play(SOUNDS[name])

  elif name in MUSIC.keys():
    pygame.mixer.music.load(MUSIC[name])
    pygame.mixer.music.set_volume(LEVELS[0])
    pygame.mixer.music.play()

init()
