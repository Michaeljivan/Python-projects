# Import files
import math
import random
import pygame
import sys
from fruit import *
from game import *
from turret import *
from bullet import *

# Top level Constants
FPS = 30
WINDOWWIDTH = 480
WINDOWHEIGHT = 640
GAMETITLE = "Python Fruit Game"

# Colors
WHITE = [255,255,255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
BLACK = [0, 0, 0]
SPEED = 0.5

# Methods
def main():
	game = Game()

	pygame.init()
	clock = pygame.time.Clock()
	surface = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
	pygame.display.set_caption(GAMETITLE)

# Main Game Loop
game_over = False
live_fruit_sprites = pygame.sprite.Group()
ticktock = 1

while (game_over==False):
	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN):
			if(event.type == pygame.K_ESCAPE):
				game_over = True
	
	if (ticktock % (FPS/SPEED) == 1):
		if (len(live_fruit_sprites) < 10):
			live_fruit_sprites.add((Fruit(WINDOWWIDTH)))

	surface.fill(BLACK)
	for sprite in live_fruit_sprites:
		sprite.update_position(SPEED, WINDOWHEIGHT, game)

	live_fruit_sprites.draw(surface)
	pygame.display.update()
	ticktock += 1
	clock.tick(FPS)

if __name__ == '__main__':
	main()