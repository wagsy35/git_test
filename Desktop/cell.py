from cs1lib import *
from random import uniform, randint

WINDOW_SIZE = 320
PIXEL_PER_CELL = 40
NUMBER_CELL_WIDTH = WINDOW_SIZE / PIXEL_PER_CELL
NUMBER_CELL_HEIGHT = WINDOW_SIZE / PIXEL_PER_CELL

x = 0
y = 0

red = 1
green = 1
blue = 1

cell_list = []
cell_table = []
cell_color = []
pick_cell = []
pick_color = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (0, 0, 0)]


FRAMERATE = 1

press = False

class cell(object):
	def __init__(self, x, y, w, h, r = 1, g = 1, b = 1):
		self.x = x
		self.y = y
		self.w = w
		self.h = h	
		self.r = r
		self.g = g
		self.b = b
	
	def draw(self):
		set_fill_color(self.r, self.g, self.b)
		draw_rectangle(self.x, self.y, self.w, self.h)

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"

class table(cell):
	def __init__(self, row, col):
		pass		

	def draw_table():
		pass

def on_click(mx, my):
	global cx, cy, pick_cell
	print("Mouse click! " + str(mx) + " " + str(my))
	pick_cell.append((mx, my))
	print(pick_cell)

def main():
	global x, y, red, green, blue, pick_cell, pick_color, PIXEL_PER_CELL, NUMBER_CELL_WIDTH	
	
	cell_list = []
	cell_table = []
	cell_color = []

	clear()
	
	#random color
	#red = uniform(0, 1)
	#green = uniform(0, 1)
	#blue = uniform(0, 1)
	
	# create table
	for c in range(int(NUMBER_CELL_WIDTH ** 2)):
		if x < WINDOW_SIZE and y < WINDOW_SIZE:
			Cell = cell(x, y, PIXEL_PER_CELL, PIXEL_PER_CELL)
			cell_table.append(Cell)
			x += PIXEL_PER_CELL
			if x == WINDOW_SIZE:
				x = 0
				y += PIXEL_PER_CELL
			if y == WINDOW_SIZE:
				y = 0
	
	cell_list += cell_table
	
	# fill cell
	for c in range(len(cell_table)):
		for p in range(len(pick_cell)):
			if pick_cell[p][0] >= cell_table[c].x and pick_cell[p][0] < cell_table[c].x + 40 \
			and pick_cell[p][1] >= cell_table[c].y and pick_cell[p][1] < cell_table[c].y + 40:
				cell_table[c].r = red
				cell_table[c].g = green
				cell_table[c].b = blue
		cell_table[c].draw()

	# create color to fill cell
	y_color = 0
	for color in range(len(pick_color)):
		Cell = cell(360, y_color, PIXEL_PER_CELL, PIXEL_PER_CELL)
		Cell.r = pick_color[color][0]
		Cell.g = pick_color[color][1]
		Cell.b = pick_color[color][2]
		cell_color.append(Cell)
		cell_color[color].draw()
		y_color += 40

	cell_list += cell_color

	# pick color to fill cell
	for c in range(len(cell_color)):
		for p in range(len(pick_cell)):
			if pick_cell[p][0] >= cell_color[c].x and pick_cell[p][0] < cell_color[c].x + 40 \
			and pick_cell[p][1] >= cell_color[c].y and pick_cell[p][1] < cell_color[c].y + 40:
				red = cell_color[c].r
				green = cell_color[c].g
				blue = cell_color[c].b
	
start_graphics(main, mouse_press=on_click)
