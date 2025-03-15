import pygame
from  constants import *

def main():
	pygame.init
	fps_clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True: #game loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		pygame.display.flip()
		dt = fps_clock.tick(60) / 1000
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
	main()
