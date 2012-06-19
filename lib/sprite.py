import pygame, ConfigParser
#from rpglib import img

class Sprite(pygame.sprite.Sprite): #Sprite class
  def __init__(self, image, posXY=(0,0)):
    """Initlize sprite class"""
    pygame.sprite.Sprite.__init__(self)
    
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = posXY
    self.custom = {}
    
  def update(self, x=0, y=0):
    self.rect = self.rect.move(x,y)
    
class Group(pygame.sprite.Group): #Group class to manage sprites
  def __init__(self):
    pygame.sprite.Group.__init__(self)
