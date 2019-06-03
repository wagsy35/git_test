import pygame, sys, os, math
from pygame.locals import *
from random import randint, shuffle

class window(object):
	"""docstring for window"""
	def __init__(self, width, height, title, color, framerate=40):
		self.width = width
		self.height = height
		self.title = title
		self.color = color
		self.framerate = framerate

	def draw(self):
		pygame.display.set_mode((self.width, self.height), 0, 32).fill(self.color)
		pygame.display.set_caption(self.title)

	def quit(self):
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

	def update(self):
		pygame.display.update()
		pygame.time.Clock().tick(self.framerate)


class image(object):
	"""docstring for image"""
	def __init__(self, path, x, y, vector, direction):
		self.path = path
		self.x = x
		self.y = y
		self.direction = direction
		self.image, self.rect = self.load_image()
		self.vector = vector

	def draw(self):
		screen = pygame.display.get_surface()
		screen.blit(self.image, (self.x, self.y))
		#print(self.rect)

	def load_image(self):
		image = pygame.image.load(self.path)
		return image, image.get_rect()

	def move(self):
		newpos = self.new_pos(self.vector)
		(angle,z) = self.vector
		self.x += newpos[0]
		self.y += newpos[1]
		self.rect[0] = self.x
		self.rect[1] = self.y
		area = pygame.display.get_surface().get_rect()
		if not area.contains(self.rect):
			tl = not area.collidepoint(self.rect.topleft)
			tr = not area.collidepoint(self.rect.topright)
			bl = not area.collidepoint(self.rect.bottomleft)
			br = not area.collidepoint(self.rect.bottomright)
			if tr and tl or (br and bl):
				angle = -angle
			if tl and bl:
				#self.offcourt()
				angle = math.pi - angle
			if tr and br:
				angle = math.pi - angle
				#self.offcourt()
		self.vector = (angle,z)

	def new_pos(self, vector):
		(angle, speed) = vector
		(dx, dy) = (speed * math.cos(angle), speed * math.sin(angle))
		return dx, dy

class icon(object):
	"""docstring for icon"""
	def __init__(self, colors, shapes):
		self.colors = colors
		self.shapes = shapes
		self.icons = self.create()

	def draw(self):
		x, y, r, w, h = 20, 20, 20, 40, 40
		screen = pygame.display.get_surface()
		for icon in self.icons:
			if icon[1] == 'donut':
				pygame.draw.circle(screen, icon[0], (x + r, y + r), r)
			elif icon[1] == 'square':
				pygame.draw.rect(screen, icon[0], (x, y, w, h))
			elif icon[1] == 'diamond':
				pygame.draw.polygon(screen, icon[0], ((x + r, y), (x + w, y + r), (x + r, y + w), (x, y + r)))
			elif icon[1] == 'lines':
				for i in range(0, w, 4):
					pygame.draw.line(screen, icon[0], (x, y + i), (x + i, y))
					pygame.draw.line(screen, icon[0], (x + i, y + w), (x + w, y + i))
			elif icon[1] == 'oval':
				pygame.draw.ellipse(screen, icon[0], (x, y + int(h/4), w, r))
			x += 50
			if x >= 360:
				x = 20
				y += 50

	def create(self):
		icons = []
		for color in self.colors:
			for shape in self.shapes:
				icons.append((color, shape))
		shuffle(icons)
		return icons


class ball(object):
	"""docstring for ball"""
	def __init__(self, x, y, radius, color):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color

	def draw(self):
		screen = pygame.display.get_surface()

		
	def move(self):
		pass


class Ball(pygame.sprite.Sprite):
	"""A ball that will move across the screen
	Returns: ball object
	Functions: update, calcnewpos
	Attributes: area, vector"""

	def __init__(self, vector):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = self.load_png('Desktop/ball.png')
		screen = pygame.display.get_surface()
		self.area = screen.get_rect()
		self.vector = vector
		self.hit = 0

	def load_png(name):
		""" Load image and return image object"""
		fullname = os.path.join('data', name)
		image = pygame.image.load(fullname)
		if image.get_alpha is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
		return image, image.get_rect()

	def update(self):
		newpos = self.calcnewpos(self.rect,self.vector)
		self.rect = newpos
		(angle,z) = self.vector

		if not self.area.contains(newpos):
			tl = not self.area.collidepoint(newpos.topleft)
			tr = not self.area.collidepoint(newpos.topright)
			bl = not self.area.collidepoint(newpos.bottomleft)
			br = not self.area.collidepoint(newpos.bottomright)
			if tr and tl or (br and bl):
				angle = -angle
			if tl and bl:
				#self.offcourt()
				angle = math.pi - angle
			if tr and br:
				angle = math.pi - angle
				#self.offcourt()
		else:
			# Deflate the rectangles so you can't catch a ball behind the bat
			player1.rect.inflate(-3, -3)
			player2.rect.inflate(-3, -3)

			# Do ball and bat collide?
			# Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
			# iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
			# bat, the ball reverses, and is still inside the bat, so bounces around inside.
			# This way, the ball can always escape and bounce away cleanly
			if self.rect.colliderect(player1.rect) == 1 and not self.hit:
				angle = math.pi - angle
				self.hit = not self.hit
			elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
				angle = math.pi - angle
				self.hit = not self.hit
			elif self.hit:
				self.hit = not self.hit
		self.vector = (angle,z)

	def calcnewpos(self,rect,vector):
		(angle,z) = vector
		(dx,dy) = (z*math.cos(angle),z*math.sin(angle))
		return rect.move(dx,dy)