from PyQt5.QtOpenGL import QGLWidget

from OpenGL.GL import *
from OpenGL.GLU import *

import gl_primitives as prm


class GLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.startTimer(100)
        self.text = 'GL_POINT'

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(0, 0, -1.0)
        glColor3f(1.0, 1.5, 0.0)
        glPolygonMode(GL_FRONT, GL_FILL)

        # scale = 0.001

        if self.text == 'GL_POINT':
            print('GL_POINT')
            prm.draw_point(10, [.1, .1, .5], [0, 0, 0], False)
        if self.text == 'GL_LINES':
            print('GL_LINES')
            prm.draw_line(5, [1., .5, 1.], [0, 0, 0], [0.3, 0.1, 0], False)
        if self.text == 'GL_LINE_STRIP':
            # print('GL_LINE_STRIP')
            prm.draw_line_strip(20, [1, 0, 0], [50, 200, 0], [200, 350, 0], False,
            [250, 550,0], [400, 380,0], [150, 60, 0])
        if self.text == 'GL_LINE_LOOP':
            # print('GL_LINE_LOOP')
            prm.draw_line_loop(20, [0, 1, 0.9], [0, 220, 0], [180, 380, 0], False,
            [290, 590,0], [420, 390,0], [190, 130, 0])
        if self.text == 'GL_TRIANGLES':
            # print('GL_TRIANGLES')
            prm.draw_triangle(15, [0.2, 0.3, 0.8], , False, 'fill')
        if self.text == 'GL_TRIANGLE_STRIP':
            # print('GL_TRIANGLE_STRIP')
            prm.draw_triangle_strip(10, [.5, 0.1, 0.6], [[420, 600, 0],[30, 510, 0],
            [70, 70, 0],[250, 250, 0]],  False, 'line')
        if self.text == 'GL_TRIANGLE_FAN':
            # print('GL_TRIANGLE_FAN')
            prm.draw_triangle_fan(50, [.4, 0.2, 0.7], [[420, 600, 0],[30, 510, 0],
            [70, 70, 0],[250, 250, 0]],  False, 'line')
        if self.text == 'GL_QUADS':
            # print('GL_QUADS')
            prm.draw_quad(30, [0.1, 0.8, 0.2], [[500, 500, 0],[580, 500, 0],
            [600, 20, 0],[450, 20, 0]], False, 'line')
        if self.text == 'GL_QUAD_STRIP':
            # print('GL_QUAD_STRIP')
            prm.draw_quad_strip(30, [0.9, 0.5, 0.2], [[500, 500, 0],[460, 500, 0],
            [600, 20, 0],[280, 280, 0],[450, 20, 0], [40, 70, 0]], False, 'line')
        if self.text == 'GL_POLYGON':
            # print('GL_POLYGON')
            prm.draw_polygon(15, [0.0, 0.4, 0.2], [[500, 500, 0],[560, 420, 0],
            [510, 380, 0],[470, 280, 0],[400, 210, 0], [290, 310, 0]], False, 'line')

        glFlush()

    def initializeGL(self):
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, 1.33, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def timerEvent(self, event):
        self.update()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)

    def changeFigure(self, text):
        self.text = text
