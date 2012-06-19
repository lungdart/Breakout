import pygame, sys
from lib import display, clock, events, board, menu

GAME = None

def loop():

    #Initilize the screen, battlefield and set semi-global variables
    screen = display.init((1280,780), "Any-bit Paddle")

    global GAME
    GAME = menu.Intro(screen)
    GAME.play()
    
    while True:
        
        #Wait to keep game at 60FPS if possible.
        clock.tick(60)

        #List new events and tie them to actions
        events.hook()
        update( screen, GAME.update() )


        #Redraw the screen, and refresh it
        screen.fill((255,255,255))
        GAME.draw()
        display.update()

def update(surface, status):
  """Update the game based on new game status"""
  global GAME
  #No change
  if status == 0: pass
  
  #Back to main menu - NO SOUND UPDATE
  if status == 1:
    GAME = menu.Intro(surface)
    
  #Back to main menu - SOUND UPDATE
  if status == 2:
    GAME = menu.Intro(surface)
    GAME.play()
  
  #Options menu  
  if status == 10:
    GAME = menu.Options(surface)
  
  #Difficulty menu  
  if status == 20:
    GAME = menu.Difficulty(surface)
  
  #Change difficulty to easy
  if status == 21:
    board.DIFFICULTY = 'easy'
    GAME = menu.Intro(surface)
    
  #Change difficulty to medium  
  if status == 22:
    board.DIFFICULTY = 'medium'
    GAME = menu.Intro(surface)

  #Change difficulty to hard 
  if status == 23:
    board.DIFFICULTY = 'hard'
    GAME = menu.Intro(surface)
    
  #Change difficulty to insane 
  if status == 24:
    board.DIFFICULTY = 'insane'
    GAME = menu.Intro(surface)
  
  #Load new level
  if status == 50:
    GAME = board.Handle(surface)
    GAME.play()
    
  #Game Over
  if status == 80:
    board.reset()
    GAME = menu.Death(surface)
    GAME.play()    
    
  if status == 99:
    print "Quitting..."
    pygame.quit()
    sys.exit()
  
