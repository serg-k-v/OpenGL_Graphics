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

        if self.text == 'GL_POINT':
            print('GL_POINT')
            prm.draw_point(10, [.1, .1, .5], [0, 0, 0], False)
        if self.text == 'GL_LINES':
            print('GL_LINES')
        if self.text == 'GL_LINE_STRIP':
            print('GL_LINE_STRIP')
        if self.text == 'GL_LINE_LOOP':
            print('GL_LINE_LOOP')
        if self.text == 'GL_TRIANGLES':
            print('GL_TRIANGLES')
        if self.text == 'GL_TRIANGLE_STRIP':
            print('GL_TRIANGLE_STRIP')
        if self.text == 'GL_TRIANGLE_FAN':
            print('GL_TRIANGLE_FAN')
        if self.text == 'GL_QUADS':
            print('GL_QUADS')
        if self.text == 'GL_QUAD_STRIP':
            print('GL_QUAD_STRIP')
        if self.text == 'GL_POLYGON':
            print('GL_POLYGON')

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
