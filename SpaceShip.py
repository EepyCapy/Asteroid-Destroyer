class SpaceShip:
	def __init__(self, colour, mainVertex, width=1):
		self.colour = colour
		self.verteces = [mainVertex, 
				   		 [mainVertex[0]-10, mainVertex[1]+25],
						 [mainVertex[0]+10, mainVertex[1]+25]]
		self.width = width
        
	def moveBy(self, dx, dy):
		for vertex in self.verteces:
			vertex[0] += dx
			vertex[1] += dy
		