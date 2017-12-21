import pyglet
from pyglet.gl import *
 
height = 800
width = 600
zs = 25 #zshift
win = pyglet.window.Window(height, width)
 
def square(x0, y0, l):
    glBegin(GL_LINES)

    glVertex2i(x0, y0)
    glVertex2i(x0, y0+l)

    glVertex2i(x0, y0+l)
    glVertex2i(x0+l, y0+l)

    glVertex2i(x0+l,y0+l)
    glVertex2i(x0+l,y0)

    glVertex2i(x0+l,y0)
    glVertex2i(x0,y0)

    glEnd()

def cube(x0, y0, l):
    glBegin(GL_LINES)

    glVertex2i(x0, y0)
    glVertex2i(x0, y0+l)

    glVertex2i(x0, y0+l)
    glVertex2i(x0+l, y0+l)

    glVertex2i(x0+l,y0+l)
    glVertex2i(x0+l,y0)

    glVertex2i(x0+l,y0)
    glVertex2i(x0,y0)

    glVertex2i(x0+l, y0+l)
    glVertex2i(x0+l+zs, y0+l+zs)
   
    glVertex2i(x0+l, y0)
    glVertex2i(x0+l+zs, y0+zs)

    glVertex2i(x0, y0+l)
    glVertex2i(x0+zs, y0+l+zs)

    glVertex2i(x0+l+zs, y0+l+zs)
    glVertex2i(x0+zs, y0+l+zs)

    glVertex2i(x0+l+zs, y0+l+zs)
    glVertex2i(x0+l+zs, y0+zs)

    glEnd()

def grid():
    sizey = height / 10
    sizex = width / 10
    for i in range(0,int(sizex)):
        for j in range(0,int(sizey)):
            square(i*50,j*50,50) 

@win.event
def on_draw():
 
        # Clear buffers
        glClear(GL_COLOR_BUFFER_BIT) 
        cube(400,300, 50)
        cube(450,300,50)
        cube(550, 300,50)
        cube(400, 350, 50)


pyglet.app.run()
