from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from gl_implement.gl_primitives import draw_triangle

import numpy as np
width, height = 900,900

tr_side = 1.5
alpha = np.pi/2

rotate_mtr_on_z = np.array([[np.cos(alpha),-np.sin(alpha),0],[np.sin(alpha),np.cos(alpha),0],[0,0,1]])

shift_right = lambda ord : np.array([(11/18)*tr_side*(3/5), 0, 0])
shift_up = lambda ord : np.array([0, (0.34)*tr_side*(3/5), 0])
shift_down = lambda ord : np.array([0, -(0.34)*tr_side*(3/5), 0])

def rotation(coords) :
    return coords.dot(rotate_mtr_on_z)

def draw_fractal(order, max_order, tr_coords) :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for coord in tr_coords:
        draw_triangle(3., [.1, .5, .1, 1], coord, False, 'line')

    tr_coords = rotation(tr_coords)*0.6
    new_obj = tr_coords.copy()
    tr_coords = np.concatenate((tr_coords + shift_up(order), tr_coords + shift_down(order)))
    tr_coords = np.concatenate((tr_coords, new_obj + shift_right(order)))

    order += 1
    if order != max_order :
        return draw_fractal(order, max_order, tr_coords)


def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    max_order = 9
    tr_coords = np.array([[
    [-tr_side/2, -tr_side/2, 0],
    [tr_side/2, -tr_side/2, 0],
    [0, tr_side/2, 0]
    ]])


    draw_fractal(0,max_order, tr_coords)

    glPointSize(3)
    glColor3d(255,255,255)
    glBegin(GL_POINTS)
    glVertex3f(0,0,0)
    glEnd()
    # draw_triangle(3., [.1, .5, .1, 1], tr_coords + shift_left, False, 'line')
    # draw_triangle(3., [.1, .5, .1, 1], tr_coords + shift_up +shift_left/2, False, 'line')
    glutSwapBuffers()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(0.0, width, 0.0, height, -1.0, 1.0)
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
