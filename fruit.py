# Imports
import pygame
import random

# Class
class Fruit(pygame.sprite.sprite):

	# Init function
	def __init__(self, WINDOWWIDTH):
		pygame.sprite.Sprite.__init__(self)
		self.species = random.choice(["raspberry", "strawberry", "cherry", "pear", "banana"])
		self.image = pygame.image.load("images/"+self._species+".png")
		self.rect = self.image.get_rect()
		self.rect.y = 0 - self.rect.height
		self.rect.x = (random.randint(self.rect.width/2, (WINDOWWIDTH - self.rect.width)))

	# Update Position function
	def update_position(self, speed, WINDOWHEIGHT, game):
		if(self.rect.y < (WINDOWHEIGHT)):
			self.rect.y += (speed * 5)
		else:
			if (self._species == "raspberry"):
				game.update_score(50)
				game.update_raspberries_saved()
			else:
				game.update_score(-10)
			self.kill()

	# Shot function
	def shot(self, game):
		if(self._species == "raspberry"):
			game.update_score(-50)
		else:
			game.update_score(10)
		self.kill()