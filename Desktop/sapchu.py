import pygame, sys, random, time
from pygame.locals import *
from graphics import *

#set up window
window_width = 600
window_height = 600
title = 'SAP CHU'
fps = 30
bgcolor = (0, 0, 0)

#set up font
font_name = 'freesansbold.ttf'
font_size_normal = 18
font_size_big = 100

#set up board
blank = '.'

L_template =       [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]

T_template =       [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                     '.....']]


template = (L_template, T_template)


def main():
	global basic_font, title_font, list_box, bo, surf, countx, county, shape_template, shape_rotation

	canvas = window(window_width, window_height, title, bgcolor, fps)
	canvas.draw()

	surf = pygame.display.get_surface()

	basic_font = pygame.font.Font(font_name, font_size_normal)
	title_font = pygame.font.Font(font_name, font_size_big)

	shadowSurf = title_font.render(title, True, (200, 200, 200))
	shadowRect = shadowSurf.get_rect()
	shadowRect.center = (int(window_width / 2), int(window_height / 2))

	titleSurf = title_font.render(title, True, (255, 255, 255))
	titleRect = titleSurf.get_rect()
	titleRect.center = (int(window_width / 2) - 3, int(window_height / 2) - 3)

	pressKeySurf = basic_font.render('Press any key to continue', True, (255, 255, 255))
	pressKeyRect = pressKeySurf.get_rect()
	pressKeyRect.center = (int(window_width / 2), int(window_height / 2) + 100)

	next_screen = None
	while next_screen == None:
		canvas.fill()
		
		for event in pygame.event.get():
			if event.type == KEYUP:
				next_screen = event.key

		surf.blit(shadowSurf, shadowRect)
		surf.blit(titleSurf, titleRect)
		surf.blit(pressKeySurf, pressKeyRect)

		canvas.update()


	bo = board(206, 406, (0, 255, 0), 4)
	'''for col in range(int(200 / 20)):
		bo.data.append([])
		for row in range(int(400 / 20)):
			bo.data[col].append(random.choice(('a', blank)))'''
	for col in range(int(200 / 20)):
		bo.data.append([blank] * int(400 / 20))

	newPiece()

	a = time.time()
	b = 0.27 - (1 * 0.02)

	while  True:
		canvas.fill()
		canvas.quit()
		bo.draw()
		drawPiece()

		if isOnBoard(shape_rotation):

			if isValidPosition(shape_rotation, dy=1):

				for event in pygame.event.get():
					if event.type == KEYUP:
						
						if event.key == K_LEFT and isOnBoard(shape_rotation, dx=-1) and isValidPosition(shape_rotation, dx=-1):
							removePiece()
							countx -= 1
							for box in list_box:
								box[0] -= 1
								bo.data[box[0]][box[1]] = 'O'

						elif event.key == K_RIGHT and isOnBoard(shape_rotation, dx=1) and isValidPosition(shape_rotation, dx=1):
							removePiece()
							countx += 1
							for box in list_box:
								box[0] += 1
								bo.data[box[0]][box[1]] = 'O'

						elif event.key == K_UP:
							removePiece()

							if shape_rotation < len(shape_template) - 1:
								temp_rotation = shape_rotation % len(shape_template) + 1
							else:
								temp_rotation = 0

							if isOnBoard(temp_rotation) and isValidPosition(temp_rotation):
								shape_rotation = temp_rotation

							Piece(shape_rotation)

				if time.time() - a > b:
					removePiece()
					county += 1
					for box in list_box:
						box[1] += 1
						bo.data[box[0]][box[1]] = 'O'
					a = time.time()

			else:
				for box in list_box:
					bo.data[box[0]][box[1]] = 'OK'
				removeCompleteLines()
				newPiece()				

		else:
			for box in list_box:
				bo.data[box[0]][box[1]] = 'OK'
			removeCompleteLines()
			newPiece()

		canvas.update()


def drawPiece():
	for col in range(int(200 / 20)):
		for row in range(int(400 / 20)):
			if bo.data[col][row] != blank:
				pygame.draw.rect(surf, (200, 200, 200), (col * 20 + bo.left + 3, row * 20 + bo.top + 5, 19, 19))
				pygame.draw.rect(surf, (255, 255, 255), (col * 20 + bo.left + 3, row * 20 + bo.top + 5, 17, 17))


def getListBox(rotation):
	lb = []
	for x in range(5):
		for y in range(5):
			if shape_template[rotation][y][x] != blank:
				boxx, boxy = int(200 / 20 / 2) - int(5 / 2) + x + countx, y - 1 + county
				lb.append([boxx, boxy])
	return lb


def isOnBoard(rotation, dx = 0, dy = 0):
	lb = getListBox(rotation)
	for box in lb:
		if box[0] + dx >= 0 and box[0] + dx < 10 and box[1] < 19:
			continue
		else:
			return False
	return True


def isValidPosition(rotation, dx=0, dy=0):
	lb = getListBox(rotation)
	for box in lb:
		if bo.data[box[0] + dx][box[1] + dy] == 'OK':
			return False
	return True


def completeLines():
	count_box = 0
	count_complete_line = 0
	list_row_complete = []
	for row in range(int(400 / 20)):
		for col in range(int(200 / 20)):
			if bo.data[col][row] == 'OK':
				count_box += 1

		if count_box == int(200 / 20):
			count_complete_line += 1
			list_row_complete.append(row)
		count_box = 0

	return count_complete_line, list_row_complete


def removeCompleteLines():
	complete_lines, list_row_complete = completeLines()
	for row in list_row_complete:
		for col in range(int(200 / 20)):
			bo.data[col][row] = blank

		for line in range(row - 1, 0, -1):
			for col in range(int(200 / 20)):
				if bo.data[col][line] == 'OK':
					bo.data[col][line] = blank
					bo.data[col][line + 1] = 'OK'


def removePiece():	
	for box in list_box:
		bo.data[box[0]][box[1]] = blank


def Piece(rotation):
	global list_box
	list_box = []

	for x in range(5):
		for y in range(5):
			if shape_template[rotation][y][x] != blank:
				boxx, boxy = int(200 / 20 / 2) - int(5 / 2) + x + countx, y - 1 + county
				list_box.append([boxx, boxy])
				bo.data[boxx][boxy] = 'O'

def newPiece():
	global list_box, countx, county, shape_template, shape_rotation
	countx = 0
	county = 0
	shape_template = random.choice(template)
	shape_rotation = random.randint(0, len(shape_template) - 1)

	Piece(shape_rotation)
	

main()