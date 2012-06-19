import pygame, sys
from pygame.locals import *

class Handle():
  def __init__(self):
    """ Initilize variables, and bindings"""
    
    #Class Varaibles
    self.bound = {}
    self.pressed = []
    self.held = []
        
    #Default keybindings. Can be changed by calling bind(value, key)    
    self.bind("ACTION", pygame.K_RETURN)
    self.bind("CANCEL", pygame.K_ESCAPE)
     
    self.bind("LEFT", pygame.K_LEFT)
    self.bind("RIGHT", pygame.K_RIGHT)
    self.bind("UP", pygame.K_UP)
    self.bind("DOWN", pygame.K_DOWN)
    
    self.bind("LEFT", pygame.K_a)
    self.bind("RIGHT", pygame.K_d)
    self.bind("UP", pygame.K_w)
    self.bind("DOWN", pygame.K_s)
    
  def bind(self, value, key):
    """ bind a key to a value to call in the game """
    
    #Add value to dict if not allready there  
    if not value in self.bound.iterkeys():
      self.bound[value] = []
      
    #Add key binding to the value in dict
    self.bound[value].append(key)

  def hook(self):
    """ Call to check for hooked events """
    
    self.pressed = [] #Reset pressed keys each call
    events = pygame.event.get() #Retrieve a list of events
    
    #For each event...
    for e in events:
      
      #Check for exit event, and quit the game
      if e.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      #Check for keys that have been pushed
      if e.type == KEYDOWN:
        self.pressed.append(e.key) #Mark the key as pressed
        self.held.append(e.key) #Mark the key as held
        
      #Check for keys that have been released
      if e.type == KEYUP:
        if e.key in self.held:
          self.held.remove(e.key) #Mark the key as released from being held
          
  def get(self, value, state=0):
    
    keys = self.bound[value]
    
    for i in keys:
      if state == 0:
        if i in self.pressed:
          return 1
        
      if state == 1:
        if i in self.held:
          return 1
        
    return 0

#Initiate Handle class and use shortcuts for simplicity
EVENTS = Handle()
bind = EVENTS.bind
hook = EVENTS.hook
get = EVENTS.get
