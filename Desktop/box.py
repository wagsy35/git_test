from graphics import *

#color code
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

'''init variables for program'''
#for window
WINDOW_WIDTH = 800		#width of window
WINDOW_HEIGHT = 600		#height of window
TITLE = "Something Like ..."	#title window
BGCOLOR = (0, 0, 0)		#color for background
FPS = 60	#frame rate

#for image
BALL = "Desktop/ball.png" #path of the image
#BALL2 = "Desktop/ball.png" #path of the image
ballx = 200	#init coord x of image
bally = 00		#init coord y of image
direction = 'upright'	#init direction to moving
speed = 10
radian = 35 * math.pi / 180
vector = (radian, speed)

#for shape
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)


def main():
	#init object for program
	Window = window(WINDOW_WIDTH, WINDOW_HEIGHT, TITLE, BGCOLOR, FPS)	#set up window
	Ball1 = image(BALL, ballx, bally, vector, direction)		#set up image
	Ball2 = image(BALL, ballx + 100, bally + 400, (radian + 0.2, speed), direction)
	Icon = icon(ALLCOLORS, ALLSHAPES)	#set up icon

	while True: #main loop
		Window.draw()	#fill new color for window
		Ball1.draw()	#draw the image at current position
		Ball1.move()	#update new image position
		Ball2.draw()
		Ball2.move()
		Icon.draw()	#draw the icon from color and shape
		Window.quit()	#handling event loop whenever you press key ESC
		Window.update()	#change state

if __name__ == '__main__':
	main()