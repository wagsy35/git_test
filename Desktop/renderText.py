import pygame, sys, random
from pygame import *

font_name = 'freesansbold.ttf'
font_size = 20
msg = 'Just for text'
antialias = 1
color = (0, 0, 0)

def main():
	pygame.init()

	screen = pygame.display.set_mode((400, 400))
	pygame.display.set_caption('Window')

	setFont = pygame.font.Font(font_name, font_size)
	textFont = setFont.render(msg, antialias, color)
	rectFont = textFont.get_rect()
	rectFont.topleft = (20, 20)

	firstRect = pygame.Rect(50, 200, 100, 100)
	secondRect = pygame.Rect(200, 200, 100, 100)

	result = None
	computerTurn = True
	pattern = []
	click = []

	while True:
		screen.fill((255, 255, 255))
		screen.blit(textFont, rectFont)

		pygame.draw.rect(screen, color, (200, 200, 100, 100))
		pygame.draw.rect(screen, color, (50, 200, 100, 100))
		

		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
				pygame.quit()
				sys.exit()

			if computerTurn:
				pattern.append(random.choice((firstRect, secondRect)))
				for choice in pattern:
					pygame.draw.rect(screen, (255, 255, 0), choice)
				computerTurn = False
				print(pattern)

			else:
				if event.type == MOUSEBUTTONUP:
					if firstRect.collidepoint(event.pos):
						print('Clicked first')
						pygame.draw.rect(screen, (255, 255, 0), (50, 200, 100, 100))
						click.append(firstRect)
					elif secondRect.collidepoint(event.pos):
						print('Clicked second')
						pygame.draw.rect(screen, (255, 255, 0), (200, 200, 100, 100))
						click.append(secondRect)
					print(click)

				if len(pattern) == len(click):
					computerTurn = True

		if len(pattern) == len(click):
			for choice in range(len(pattern)):
				if click[choice] == pattern[choice]:
					result = True
				else:
					result = False
					break

			if result:
				print('win')
				click = []
			else:
				print('lose')
				pattern = []
				click = []
					

		pygame.display.update()
		pygame.time.Clock().tick(30)

main()

