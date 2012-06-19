import pygame, events, noise, img, sys, os

class Menu():
  def __init__(self, surface, title, selections=None):
    #Current selection
    self.selection = 0
    
    #Set the wallpaper
    self.surface = surface
    self.wallPaper = img.load(self.surface, os.path.join('content','images','bg','menu.jpg'))
    
    #Set the music
    self.music = 'menu'
    
    #Title
    self.titleLL = pygame.Surface((750, 100), flags=pygame.SRCALPHA)
    self.titleLL.fill((0,0,0,100))
    self.titleFont = pygame.font.Font(None, 64)
    self.titleText = self.titleFont.render(title,0,(255,255,255))
    #Set Title locations
    self.titleTextRect = self.titleText.get_clip()
    self.titleLLRect = self.titleLL.get_clip()
    self.titleLLRect.centerx = 640
    self.titleLLRect.top = 100
    self.titleTextRect.center = self.titleLLRect.center
    
    #Menu Choices
    self.selectLL = pygame.Surface((500, 300), flags=pygame.SRCALPHA)
    self.selectLL.fill((0,0,0,100))
    self.selectFont = pygame.font.Font(None, 32)
    self.selectedFont = pygame.font.Font(None, 48)
    self.selectText = {}
    self.selectedText = {}
    #Iterate through all selections to create font surfaces
    for i in selections.keys():
      self.selectText[i] = [self.selectFont.render(selections[i][0],0,(255,255,255)), None]
      self.selectedText[i] = [self.selectedFont.render(selections[i][0],0,(255,0,0)), None, selections[i][1]]
    #Menu location                  
    self.selectLLRect = self.selectLL.get_clip()
    self.selectLLRect.centerx = 640
    self.selectLLRect.centery = ((780 - self.titleLLRect.bottom) / 2) + self.titleLLRect.bottom
    #Iterate through all selections again :/ to set locations for each selection
    for i in self.selectText.keys():
      self.selectText[i][1] =  self.selectText[i][0].get_clip()
      self.selectText[i][1].centerx = self.titleLLRect.centerx
      self.selectText[i][1].centery = (self.selectLLRect.height / (len(self.selectText)+1) * (i+1)) + self.selectLLRect.top
      self.selectedText[i][1] = self.selectedText[i][0].get_clip()
      self.selectedText[i][1].centerx = self.titleLLRect.centerx
      self.selectedText[i][1].centery = self.selectText[i][1].centery
    
  def draw(self):
    #Draw background
    self.surface.blit(self.wallPaper, (0,0))
    
    #Draw title
    self.surface.blit(self.titleLL, self.titleLLRect)
    self.surface.blit(self.titleText, self.titleTextRect)
    
    #Draw selection
    self.surface.blit(self.selectLL, self.selectLLRect)
    for i in self.selectText.keys():
      if i == self.selection: self.surface.blit(self.selectedText[i][0], self.selectedText[i][1])
      else: self.surface.blit(self.selectText[i][0], self.selectText[i][1])
  
  def play(self):
    #Start zee music!
    noise.play(self.music)
  
  def update(self):
    
    #Return selection value chosen
    if events.get("ACTION",0):
      return self.selectedText[self.selection][2]
    
    #Control selection with up/down keys
    if events.get("UP",0): self.selection -= 1
    if events.get("DOWN",0): self.selection += 1
    if self.selection < 0: self.selection = 0
    if self.selection > len(self.selectText) - 1: self.selection = len(self.selectText) - 1
    
    return 0
    
class Intro(Menu):
  def __init__(self, surface):
    
    title = "Any-bit Paddle!"
    selections = {
                 0: ["Start Game", 50],
                 1: ["Options", 10],
                 2: ["Difficulty", 20],
                 3: ["Exit to Desktop", 99]
                 }
                 
    Menu.__init__(self, surface, title, selections)
    
class Options(Menu):
  def __init__(self, surface):
    
    title = "Options"
    selections = {
                 0: ["Sound Volume", 0],
                 1: ["Music Volume", 0],
                 2: ["Clear High Score", 0],
                 3: ["Keyboard Bindings", 0]
                 }
                 
    Menu.__init__(self, surface, title, selections)
  
  def update(self):
    if events.get("CANCEL", 0): return 1
    else: Menu.update(self)

class Difficulty(Menu):
  def __init__(self, surface):
    
    title = "Difficulty"
    selections = {
                 0: ["Easy", 21],
                 1: ["Medium", 22],
                 2: ["Hard", 23],
                 3: ["Insane",24]
                 }
                 
    Menu.__init__(self, surface, title, selections)
    
  def update(self):
    if events.get("CANCEL", 0): return 1
    else: return Menu.update(self)
    
class Death(Menu):
  def __init__(self, surface):
    
    title = "GAME OVER"
    selections = {
                 0: ["Restart", 50],
                 1: ["Main Menu", 2]
                 }
                 
    Menu.__init__(self, surface, title, selections)
    
    self.music = "gameover"
  
