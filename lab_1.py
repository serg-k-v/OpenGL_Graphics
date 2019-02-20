from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import gl_primitives as prm

width, height = 640,480

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    prm.draw_point(10, [.1, .1, .5], [100, 200, 0], False)
    prm.draw_point(20, [.1, .17, .5], [50, 100, 0], False)
    prm.draw_point(40, [.3, .5, 0.5], [150, 400, 0], True)

    prm.draw_line(5, [1., .5, 1.], [50, 50, 0], [300, 100, 0], False)
    prm.draw_line(5, [1., 1., 1.], [300, 50, 0], [500, 400, 0], False)

    prm.draw_line_strip(20, [1, 0, 0], [50, 200, 0], [200, 350, 0], False,
    [250, 550,0], [400, 380,0], [150, 60, 0])

    prm.draw_line_loop(20, [0, 1, 0.9], [0, 220, 0], [180, 380, 0], False,
    [290, 590,0], [420, 390,0], [190, 130, 0])

    prm.draw_triangle(15, [0.2, 0.3, 0.8], [[500, 500, 0],[450, 20, 0],
    [600, 20, 0]], False, 'fill')
    prm.draw_triangle_fan(50, [.4, 0.2, 0.7], [[420, 600, 0],[30, 510, 0],
    [70, 70, 0],[250, 250, 0]],  False, 'line')
    prm.draw_triangle_strip(10, [.5, 0.1, 0.6], [[420, 600, 0],[30, 510, 0],
    [70, 70, 0],[250, 250, 0]],  False, 'line')

    prm.draw_quad(30, [0.1, 0.8, 0.2], [[500, 500, 0],[580, 500, 0],
    [600, 20, 0],[450, 20, 0]], False, 'line')
    prm.draw_quad_strip(30, [0.9, 0.5, 0.2], [[500, 500, 0],[460, 500, 0],
    [600, 20, 0],[280, 280, 0],[450, 20, 0], [40, 70, 0]], False, 'line')

    prm.draw_polygon(15, [0.0, 0.4, 0.2], [[500, 500, 0],[560, 420, 0],
    [510, 380, 0],[470, 280, 0],[400, 210, 0], [290, 310, 0]], False, 'line')

    glutSwapBuffers()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, -1.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glutPostRedisplay()

def Init_GL_Window(num_window, width, height) :

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(300, 300)

    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    # glutIdleFunc(draw)
    glutReshapeFunc(refresh2d)
    glClearColor(.26, .23, .51 , 1.0) # background color
    glutMainLoop()

def main() :
    Init_GL_Window(0, width, height);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
