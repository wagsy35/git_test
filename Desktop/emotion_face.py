from cs1lib import *
from random import randint
from time import sleep

emotion = "smile"
grow = True
x = 200
y = 200
r = 100

FRAMERATE = 1

emotion_face = None

#Object face
class face(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.r = radius

    def draw_face(self):
        set_fill_color(1, 1, 0)   # set fill color to yellow
        draw_circle(self.x, self.y, self.r)

    def draw_mouth_1(self):
        set_fill_color(1, 1, 0)  # yellow
        draw_circle(self.x, self.y, self.r / 1.67)
        set_stroke_color(1, 1, 0)
        draw_rectangle(self.x - (self.r / 1.4625), self.y - (self.r / 1.4625), self.r / 0.75125, self.r / 1.25)

    def draw_mouth_2(self):
        draw_line(x - r / 1.67, y + r / 3.34, x + r / 1.67, y + r / 3.34)
        
    def draw_mouth_3(self):
        set_fill_color(1, 1, 1)  # white
        draw_circle(self.x, self.y, self.r / 1.67)
        set_stroke_color(1, 1, 0)
        set_fill_color(1, 1, 0) # yellow
        draw_rectangle(self.x - (self.r / 1.4625), self.y - (self.r / 1.4625), self.r / 0.75125, self.r / 1.25)
        set_stroke_color(0, 0, 0)
        draw_line(x - r / 1.7, y + r / 9, x + r / 1.7, y + r / 9)

    def draw_eyes(self):
        set_stroke_color(0, 0, 0)
        set_fill_color(0, 0, 0)  # set fill color to black
        draw_circle(self.x - (self.r / 2.5), self.y - (self.r / 5.0), self.r / 10)
        draw_circle(self.x + (self.r / 2.5), self.y - (self.r / 5.0), self.r / 10)


#draw the emotion face

def super_stupid_face():
    # draw the outline of the face
    emotion_face.draw_face()
    emotion_face.draw_eyes()

def smile_face():
    emotion_face.draw_face()
    emotion_face.draw_mouth_1()
    emotion_face.draw_eyes()
  
def stupid_face():
    super_stupid_face()
    emotion_face.draw_mouth_2()
    
def laugh_face():
    emotion_face.draw_face()
    emotion_face.draw_mouth_3()
    emotion_face.draw_eyes()

def count_face():
    global x
    global y
    global r
    x = randint(1, 400)
    y = randint(1, 400)
    r = randint(1, 100)
    smile_face(x, y, r)
    

# draw main

def draw():

    global x, y, r, grow, emotion, emotion_face

    # draw a white background
    set_clear_color(1, 1, 1)
    clear()
    
    emotion_face = face(x, y, r)
    
    # draws the emotion faces
    #for i in range(len(emotion_face)):
    #    smile_face(emotion_face[i][0], emotion_face[i][1], r)
    if emotion == 'smile':
        smile_face()
        emotion = "stupid"
    elif emotion == 'stupid':
        stupid_face()
        emotion = "super stupid"
    elif emotion == 'super stupid':
        super_stupid_face()
        emotion = "laugh"
    else:
        laugh_face()
        emotion = "smile"
        
    #changing size of face
    '''if grow:
        r += 1
        if r == 200:
            grow = not grow
    else:
        r -= 1
        if r == 1:
            grow = not grow'''
            

start_graphics(draw, framerate=FRAMERATE)
