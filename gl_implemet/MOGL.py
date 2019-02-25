from PyQt5.QtOpenGL import QGLWidget

from OpenGL.GL import *
from OpenGL.GLU import *

from gl_implemet import gl_primitives as prm
import numpy as np

class GLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.startTimer(100)
        self.text = 'GL_POINT'

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # glOrtho(0.0, self.width(), 0.0, self.height(), -1.0, 1.0)
        # gluOrtho2D(0, self.width(), 0, self.height())
        glTranslatef(0, 0, -1.0)
        glPolygonMode(GL_FRONT, GL_FILL)

        # scale = 0.001
        if self.text == 'GL_POINT':
            # print('GL_POINT')
            prm.draw_point(10, [.1, .1, .5], [0, 0, 0], False)
        if self.text == 'GL_LINES':
            # print('GL_LINES')
            prm.draw_line(5, [1., .5, 1.], [0,0, 0], [0.3, 0.3, 0], False)
        if self.text == 'GL_LINE_STRIP':
            # print('GL_LINE_STRIP')
            prm.draw_line_strip(20, [1, 0, 0], [-.05, -.2, 0], [-.4, .35, 0], False,
            [-.25, -.4,0], [.2, .38,0], [.3, -.4, 0])
        if self.text == 'GL_LINE_LOOP':
            # print('GL_LINE_LOOP')
            prm.draw_line_loop(20, [1, 0, 0], [-.05, -.2, 0], [-.4, .35, 0], False,
            [-.25, -.4,0], [.2, .38,0], [.3, -.4, 0])
        if self.text == 'GL_TRIANGLES':
            # print('GL_TRIANGLES'
            prm.draw_triangle(15, [0.3, 0.3, 0.8], [[-.2,-.2,0], [0,0.2,0], [.2,-.2,0]] , False, 'fill')
        if self.text == 'GL_TRIANGLE_STRIP':
            # print('GL_TRIANGLE_STRIP')
            prm.draw_triangle_strip(10, [.5, 0.1, 0.6], [[-.320, .200, 0],[.030, -.300, 0],
            [.070, .070, 0],[.250, .250, 0]],  False, 'line')
        if self.text == 'GL_TRIANGLE_FAN':
            # print('GL_TRIANGLE_FAN')
            prm.draw_triangle_fan(50, [.4, 0.2, 0.7], [[-.320, .200, 0],[.030, -.300, 0],
            [.070, .070, 0],[.250, .250, 0]],  False, 'line')
        if self.text == 'GL_QUADS':
            # print('GL_QUADS')
            prm.draw_quad(30, [0.1, 0.8, 0.2], [[-.300, -.300, 0],[-.380, .300, 0],
            [.300, .300, 0],[.450, -.200, 0]], False, 'line')
        if self.text == 'GL_QUAD_STRIP':
            # print('GL_QUAD_STRIP')
            prm.draw_quad_strip(30, [0.9, 0.5, 0.2], [[-.300, .300, 0],[.360, .300, 0],
            [-.280, -.280, 0],[.300, -.2, 0],[-.34, -.34, 0],[.4, -.4,0]], False, 'line')
        if self.text == 'GL_POLYGON':
            # draw 8-corner
            r = .4
            coord = [[] , [], [], [], [], [], [], []]
            for i, k in enumerate(coord):
                x = r*np.sin(np.pi/2 + (np.pi/4)*i )
                y = r*np.cos(np.pi/2 + (np.pi/4)*i )
                coord[i] = [x,y,0]
            #
            prm.draw_polygon(15, [0.0, 0.4, 0.2], coord, False, 'fill')

        glFlush()

    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.33, 0.1, 100.0) # изменяет масштабируемость
        glMatrixMode(GL_MODELVIEW)

    def timerEvent(self, event):
        self.update()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def changeFigure(self, text):
        self.text = text
