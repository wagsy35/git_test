from cs1lib import start_graphics, clear, draw_circle, draw_rectangle, set_fill_color, set_stroke_color

def draw():
    
    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(.9, .9, .1)
    set_stroke_color(0, 0, 0)
    draw_circle(100, 100, 50)
    
    # draw the mouth
    draw_circle(100, 100, 30)
    set_stroke_color(.9, .9, .1)
    draw_rectangle(68, 68, 63, 38)
    
    # draw the eyes
    set_fill_color(0, 0, 0)
    draw_circle(80, 80, 7)
    draw_circle(120, 80, 7)
    
start_graphics(draw)
