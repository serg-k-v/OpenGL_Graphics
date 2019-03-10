from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from gl_implement.gl_primitives import draw_triangle

import numpy as np
width, height = 900,700

tr_side = .6
alpha = -np.pi/2
tr_coords = np.array([[0,0,0], [tr_side,0,0], [tr_side/2, (6/5)*np.sqrt(3/4)*tr_side, 0]])
rotate_mtr_on_z = np.array([[np.cos(alpha),-np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])
# shift = np.array([0,tr_side,0])

def rotation(coords) :
    return coords.dot(rotate_mtr_on_z)

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    for el in range(length(coords)):
        draw_triangle(3., [.1, .5, .1, 1], tr_coords, False, 'line')
        
    shift_left = np.array([(2/3)*tr_side, 0, 0])
    draw_triangle(3., [.1, .5, .1, 1], tr_coords + shift_left, False, 'line')
    # shift_up = np.array([0, (2/3)*((np.sqrt(3)/2)*tr_side), 0])
    shift_up = np.array([0, (2/3.5  )*tr_side, 0])
    draw_triangle(3., [.1, .5, .1, 1], tr_coords + shift_up +shift_left/2, False, 'line')
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
    glutInitWindowPosition(200, 200)

    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    # glutReshapeFunc(refresh2d)
    glClearColor(.26, .23, .51 , 1.0) # background color
    glutMainLoop()

def main() :
    Init_GL_Window(0, width, height);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
