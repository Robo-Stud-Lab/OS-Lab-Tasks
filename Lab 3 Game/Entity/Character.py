import pygame

WallCors = []
class Character: 

	StartingPositionX = 0
	StartingPositionY = 0
	Speed = 0
	size = [0,0]
	position = dict(x = StartingPositionX,y= StartingPositionY)


	def __init__(self):
		StartingPositionX = self.StartingPositionX
		StartingPositionY = self.StartingPositionY
		position = self.position
		

	@property
	def Position(self):
		return self.position
	

	@Position.setter
	def Position(self,x,y):
		self.position = [x,y]


	@property
	def Size(self):
		return self.size
	

	@property
	def Tile(self):
		return pygame.Rect(self.Position['x'],self.Position['y'],*self.Size)


	def DrawOn(self,surface):
		pygame.draw.rect(surface,(225, 225, 0), [self.Position['x'],self.Position['y'],*self.Size])



	def _checkObstacles(self,direction):
		if direction is 'left':
			if (self.Position['x'] - self.Speed) not in WallCors:
				return True

		if direction is 'right':
			if (self.Position['x'] +  self.Speed) not in WallCors:
				return True

		if direction is 'up':
			if (self.Position['y'] - self.Speed) not in WallCors:
				return True

		if direction is 'down':
			if (self.Position['y'] + self.Speed) not in WallCors:
				return True
	

	def GoLeft(self):
		if self._checkObstacles('left'):
			self.Position['x'] -=self.Speed
			self.Tile.move_ip(0-self.Speed,0)

	def GoRight(self):
		if self._checkObstacles('right'):
			self.Position['x'] +=self.Speed
			self.Tile.move_ip(0+self.Speed,0)

	def GoUp(self):
		if self._checkObstacles('up'):
			self.Position['y'] -=self.Speed
			self.Tile.move_ip(0,0-self.Speed)

	def GoDown(self):
		if self._checkObstacles('down') :
			self.Position['y'] +=self.Speed
			self.Tile.move_ip(0,0+self.Speed)
	