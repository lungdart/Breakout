import pygame, math, board, events, img, noise
from lib import sprite

#Globals
BALLS = None
BRICKS = None
PADDLE = None

def init(balls, bricks, paddle):
  """Initiate physics engine with sprite groups"""
  global BALLS, BRICKS, PADDLE
  BALLS = balls
  BRICKS = bricks
  PADDLE = paddle
  
def update():
  """Update ball/paddle/bricks based on physics"""
  
  #Keep track of variables changes with gameplay
  score = 0
  lives = 0

  #Update paddle location
  location = PADDLE.sprites()[0].rect.left
  offset = 0
  
  if events.get("LEFT", 0) or events.get("LEFT", 1):
    offset = -16
    if location + offset < 0: offset = 0
      
  if events.get("RIGHT", 0) or events.get("RIGHT", 1):
    offset = 16
    if location + offset > 1152: offset = 0
    
  PADDLE.sprites()[0].update(x=offset)
  
  #Update ball locations
  for i in BALLS.sprites():
    v = i.custom['v']
    
    #Collisions
    ballEdge = (i.rect.topleft[0], i.rect.topleft[1], i.rect.topleft[0]+16, i.rect.topleft[1]+16)
    collide = None
    
    #Screen edge collisions
    if ballEdge[0] <= 0 or ballEdge[2] >= 1280:
      collide = 'x'
      noise.play('bounce')
    if ballEdge[1] <= 32:
      collide = 'y'
      noise.play('bounce')
    if ballEdge[3] >= 780:
      lives = -1
      i.remove(BALLS)
      noise.play('miss')
      break
     
    collisions = pygame.sprite.spritecollide(i, BRICKS, 0) #Brick collisions
    if len(collisions) > 0:
      for j in collisions: #For each collision...

        score += 250
        j.custom['i'] -= 1
        if j.custom['i'] < 0: #Remove brick if it was the final brick
          j.remove(BRICKS)
          noise.play('break')
          
        else: #Reduce brick in toughness
          j.image = img.CACHE['brick%i' % j.custom['i']]
          noise.play('bounce')
  
        if i.rect.top <= j.rect.bottom and i.custom['v'][1] > 0: collide = 'y'
        if i.rect.bottom >= j.rect.top and i.custom['v'][1] < 0: collide = 'y'
        if i.rect.left <= j.rect.right and i.custom['v'][0] < 0 and i.rect.right > j.rect.right:
          collide = 'x'
        if i.rect.right >= j.rect.left and i.custom['v'][0] > 0 and i.rect.left < j.rect.left:
          collide = 'x'

        
    collisions = pygame.sprite.spritecollide(i, PADDLE, 0) #Paddle collision
    if len(collisions) > 0:
      paddleXY = collisions[0].rect.topleft
      paddleCenter = collisions[0].rect.centerx
      ballCenter = i.rect.centerx
      hitBox = ballCenter - paddleCenter
      newX = float(hitBox) / (paddleCenter - paddleXY[0])
      if newX > 0.45: hitPercent = 0.45
      elif newX < -0.45: hitPercent = -0.45
      
      if newX >= 0: newY = 1 - newX
      elif newX < 0: newY = 1 + newX
      
      i.custom['v'] = [newX, newY]
      noise.play('bounce')
      
    if collide == 'x': i.custom['v'][0] *= -1
    if collide == 'y': i.custom['v'][1] *= -1
    
    #Update ball location based off magnitude and rise/run
    x = int( round(i.custom['v'][0] * 16, 0) )
    y = int( round(i.custom['v'][1] * 16 * -1, 0) )
    
    i.update(x,y)
    
  return (score, lives)
    
    
