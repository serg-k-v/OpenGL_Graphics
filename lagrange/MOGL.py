from PyQt5.QtOpenGL import QGLWidget

from OpenGL.GL import *

from scipy.interpolate import lagrange


class GLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.type = 1
        self.mas = [[108.1, 234],
                  [76, 228.3],
                  [48.2, 210.5],
                  [45.2, 186.7],
                  [59.3, 171.2]]
        self.flag = False
        self.curI = 0
        self.t = [i for i in range(5, 795, 10)]
        self.f = self.Lagrange()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        self.draw()
        self.Lagrange()

    def initializeGL(self):
        glClearColor(.20, .9, .5, 1.0)  # background color
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.width(), self.height(), 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)



    def mousePressEvent(self, event):
        print('press mouse')
        x = event.pos().x()
        y = event.pos().y()
        self.curI = 0
        for elem in self.mas:
            if elem[0] - 5 < x < elem[0] + 5 and elem[1] - 5 < y < elem[1] + 5:
                print('Попал')
                self.flag = True
                break
            self.curI += 1

    def mouseMoveEvent(self, event):
        print('move mouse')
        if self.flag:
            x = event.pos().x()
            y = event.pos().y()
            self.mas[self.curI][0] = x
            self.mas[self.curI][1] = y
            self.update()
            self.f = self.Lagrange()

    def mouseReleaseEvent(self, *args, **kwargs):
        print('release mouse')
        self.flag = False

    def draw(self):
        glLineWidth(5)
        glColor3d(0, 1, 0)
        glBegin(GL_LINE_STRIP)
        for i in range(0, len(self.t)):
            glVertex3d(self.t[i], self.f[i], 0)
        glEnd()

        for elem in self.mas:
            glPointSize(10)
            glColor3d(1.0, 0, 0)
            glEnable(GL_POINT_SMOOTH)
            glBegin(GL_POINTS)
            glVertex3d(elem[0], elem[1], 0)
            glEnd()



    def Lagrange(self):
        x = [elem[0] for elem in self.mas]
        y = [elem[1] for elem in self.mas]
        L = lagrange(x, y)
        y = L(self.t)
        return y
