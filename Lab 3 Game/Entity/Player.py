import pygame as pg
import Entity.Character as Character
import config 

class Player(Character.Character):

	def __init__(self):
		super().__init__()
	
	Speed = 5
	StartingPositionX = config.WIDTH/2
	StartingPositionY =	config.HEIGHT/2

	StartingPosition = dict(x=StartingPositionX,y=StartingPositionY)
	position = dict(x = StartingPositionX,y= StartingPositionY)
	size = (100,25)
	
