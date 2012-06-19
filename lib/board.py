import pygame, os, ConfigParser
from lib import sprite, img, physics, noise

SCORE = 0
LEVEL = 0
LIVES = 3
DIFFICULTY = 'medium'

c_RED = (255,0,0)
c_ORANGE = (255,160,50)
c_YELLOW = (255,255,0)
c_BLACK = (125,125,125)

BGFile = os.path.join('content','images','wallpaper.jpg')
brickFile = os.path.join('content','images','blank_brick.png')
paddleFile = os.path.join('content','images','paddle.png')
ballFile = os.path.join('content','images','ball.png')

def reset():
  global SCORE, LEVEL, LIVES
  SCORE = 0
  LEVEL = 1
  LIVES = 3

class Handle():
  def __init__(self, surface):
    """Intilize the board"""
    #Set up the surface and groups
    self.surface = surface
    self.brickGroup = sprite.Group()
    self.paddleGroup = sprite.Group()
    self.ballGroup = sprite.Group()
    BRICK_GROUP = self.brickGroup
    
    #Setup the top score field
    global LEVEL
    LEVEL += 1
    
    self.scoreLL = pygame.Surface((1280, 32), flags=pygame.SRCALPHA)
    self.scoreLL.fill((0,0,0,100))
    self.scoreFont = pygame.font.Font(None, 24)

    self.livesText = self.scoreFont.render("Lives: %i" % LIVES, 0, (210,210,210))
    self.scoreText = self.scoreFont.render("%i Pts" % SCORE, 0, (210,210,210))
    self.levelText = self.scoreFont.render("Level %i" % LEVEL, 0, (210,210,210))
    
    #Load images into cache
    self.blankBrick = img.load(surface, brickFile)
    self.paddleImage = img.load(surface, paddleFile)
    self.ballImage = img.load(surface, ballFile)
    
    #Create brick types
    img.CACHE['brick0'] = self.blankBrick.copy()
    img.CACHE['brick1'] = self.blankBrick.copy()
    img.CACHE['brick2'] = self.blankBrick.copy()
    img.CACHE['brick3'] = self.blankBrick.copy()
    img.CACHE['brick0'].fill(c_RED, special_flags=pygame.BLEND_RGB_MIN)
    img.CACHE['brick1'].fill(c_ORANGE, special_flags=pygame.BLEND_RGB_MIN)
    img.CACHE['brick2'].fill(c_YELLOW, special_flags=pygame.BLEND_RGB_MIN)
    img.CACHE['brick3'].fill(c_BLACK, special_flags=pygame.BLEND_RGB_MIN)
    
    #Load the level
    self.load()
    physics.init(self.ballGroup, self.brickGroup, self.paddleGroup)
    
  def load(self):
    """Load images into sprites, and organize them by groups"""
    
    #load map from file
    config = ConfigParser.RawConfigParser()
    config.read(os.path.join('content','maps','%i.map' % LEVEL))
    levelMap = []
    for i in range(0,6):
      try:
        brickList = map( int, config.get(DIFFICULTY, str(i)).split(',') )
        levelMap.append(brickList)
      except: pass
    self.map = levelMap
   
    #Load background and sound for the stage
    self.music = config.get('info', 'music')
    self.wallPaper = img.load(self.surface, os.path.join('content','images','bg','%s.jpg' % config.get('info', 'bg')))
    
    #Load the bricks from the map
    total = 0
    offsetXY = [0,32]
    
 
    for r in self.map:    #For every row in the map
      offsetXY[0] = 128
      offsetXY[1] += 16
      

      for c in r:       #For every column in the row
        brick = sprite.Sprite(img.CACHE['brick%i' % c], offsetXY)
        brick.custom['i'] = c
        brick.add(self.brickGroup)
        offsetXY[0] += 64
    
    #Add paddle and ball    
    paddle = sprite.Sprite(self.paddleImage, [608, 700])
    paddle.add(self.paddleGroup)
    
    ball = sprite.Sprite(self.ballImage, [662, 684])
    ball.custom['v'] = [0,1]
    ball.add(self.ballGroup)
    
  def play(self):
    #Start zee music!
    noise.play(self.music)
        
  def update(self):
    """Update gamestate based on key presses"""
    
    #Let physics engine update objects
    new = physics.update()
    
    #Update Score/lives
    global SCORE,LIVES
    SCORE += new[0]
    LIVES += new[1]
    
    self.livesText = self.scoreFont.render("Lives: %i" % LIVES, 0, (210,210,210))
    self.scoreText = self.scoreFont.render("%i Pts" % SCORE, 0, (210,210,210))
    
    if new[1] != 0:
      ball = sprite.Sprite(self.ballImage, [662, 684])
      ball.custom['v'] = [0,1]
      ball.add(self.ballGroup)
      
      if LIVES < 0: return 80
      
    if len( self.brickGroup.sprites() ) == 0: return 1
    return None
    

  def draw(self):
    """Draw everything to the screen"""
    
    #Draw background, score board, and information
    self.surface.blit(self.wallPaper, (0,0))
    self.surface.blit(self.scoreLL, (0,0))
    self.surface.blit(self.livesText, (32, 8))
    self.surface.blit(self.scoreText, (600, 8))
    self.surface.blit(self.levelText, (1190, 8))
    

    #Draw paddle, balls, and bricks
    self.brickGroup.draw(self.surface)
    self.paddleGroup.draw(self.surface)
    self.ballGroup.draw(self.surface)
