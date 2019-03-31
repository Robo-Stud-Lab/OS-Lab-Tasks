import pygame, os, sys, inspect


current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

from config import *

import Entity.Player
Player = Entity.Player.Player()


BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
 

def LaunchGame(width=WIDTH,height=HEIGHT,caption="My Game"):
	'''
	Initialises Game
	'''
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption(caption)
	#pygame.mixer.init()  #for sound

	
	#little p in front of var means Player like pPos — player position
	pPos = Player.Position 	# list of (x,y) player position

	right = True

	# Game Loop
	main = True
	motion = []
	while main == True:

		#EVENT READING
		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()
				main == False

			if event.type == pygame.KEYDOWN:
				if event.key == ord('q'):
					pygame.quit()
					sys.exit()
					main == False


		#KEY COMMANDS		
		keys = pygame.key.get_pressed()
		
		if keys[pygame.K_LEFT]: Player.GoLeft() 
		if keys[pygame.K_RIGHT]: Player.GoRight()
		if keys[pygame.K_UP]: Player.GoUp() 
		if keys[pygame.K_DOWN]: Player.GoDown()

		#GRAPHICS INITIALIZATION
		screen.fill(BLACK)


		Player.DrawOn(screen)

		f1 = pygame.font.Font(None,18)
		F1 = f1.render('BOOOM',1, LIGHT_BLUE)

		pygame.draw.rect(screen,PINK, [100,100,200,500])
		aa = pygame.Rect(100,100,200,500)

		if Player.Tile.colliderect(aa):
			screen.blit(F1,(width/2,height/2))
			pygame.display.update()


		#Player.Tile.bottomright #for collisions


		pygame.display.update(Player.Tile)
		clock.tick(FPS)
