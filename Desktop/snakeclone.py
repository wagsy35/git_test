import pygame, sys, random
from pygame.locals import *
from graphics import *

x = 0
y = 0

snakex = 4 * 40
snakey = 8 * 40

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'

direction = RIGHT

def main():
	global x, y, snakex, snakey, direction

	food = True
	snake = [[snakex, snakey], [snakex + 40, snakey], [snakex + 80, snakey]]

	canvas = window(600, 600, 'Snake', (0, 0, 0), 15)
	canvas.draw()
	surf = pygame.display.get_surface()
	while True:
		canvas.fill()
		canvas.quit()

		if food:
			foodx = random.randint(0, int(600/40) - 1) * 40
			foody = random.randint(0, int(600/40) - 1) * 40
			food = False
		
		snakeRect = pygame.Rect(snake[-1][0], snake[-1][1], 40, 40)
		foodRect = pygame.Rect(foodx, foody, 40, 40)
		#print(snakeRect)

		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			
			if event.type == KEYUP:
				if event.key == K_RIGHT and direction != LEFT:
					direction = RIGHT
				elif event.key == K_LEFT and direction != RIGHT:
					direction = LEFT
				elif event.key == K_UP and direction != DOWN:
					direction = UP
				elif event.key == K_DOWN and direction != UP:
					direction = DOWN	
				

		for col in range(int(600/40)):
			for row in range(int(600/40)):
				pygame.draw.rect(surf, (255, 255, 255), (x, y, 40, 40), 1)
				y += 40
			x += 40
			y = 0
		x = 0

		
		pygame.draw.rect(surf, (255, 0, 0), (foodx, foody, 40, 40))

		for body in snake:
			pygame.draw.rect(surf, (0, 255, 0), (body[0], body[1], 40, 40))
			pygame.draw.rect(surf, (0, 200, 0), (body[0] + 10, body[1] + 10, 20, 20))

		#snakeRect.collidepoint(surf)
		if snakeRect.colliderect(foodRect):
			if direction == RIGHT:
				snake.append([foodx + 40, foody])
			elif direction == LEFT:
				snake.append([foodx - 40, foody])
			elif direction == UP:
				snake.append([foodx, foody - 40])
			elif direction == DOWN:
				snake.append([foodx, foody + 40])
			food = True

		for body in snake:
			if direction == RIGHT:
				if body[1] < snake[-1][1]:
					body[1] += 40
				elif body[1] > snake[-1][1]:
					body[1] -= 40
				else: 
					body[0] += 40
			elif direction == LEFT:
				if body[1] < snake[-1][1]:
					body[1] += 40
				elif body[1] > snake[-1][1]:
					body[1] -= 40
				else:
					body[0] -= 40
			elif direction == UP:
				if body[0] < snake[-1][0]:
					body[0] += 40
				elif body[0] > snake[-1][0]:
					body[0] -= 40
				else:
					body[1] -= 40
			elif direction == DOWN:
				if body[0] < snake[-1][0]:
					body[0] += 40
				elif body[0] > snake[-1][0]:
					body[0] -= 40
				else:
					body[1] += 40

		canvas.update()


main()