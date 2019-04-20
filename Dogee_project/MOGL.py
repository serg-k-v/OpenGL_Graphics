from PyQt5.QtOpenGL import QGLWidget

from OpenGL.GL import *
from OpenGL.GL.shaders import *
from glm import radians, perspective, vec3, mat4, lookAt

# from trash import arrP as arr paralels_arr
from trash import paralels_arr as paralels_
# print(len(paralels_[0,:]))
import numpy as np


class GLWidget(QGLWidget):
    def __init__(self, parent):
        QGLWidget.__init__(self, parent)

        self.vertexShader = """
                #version 130

                attribute vec3 vert;
                uniform mat4 MVP;


                void main() {
                   gl_Position = MVP * vec4(vert, 1.0);
                }
        """

        # fragment shader program
        self.fragmentShader = """
                #version 130
                uniform vec4 fragmentColor;
                out vec4 color;

                void main()
                {
                   // Output color = red
                   color = fragmentColor;
                }
        """
        self.polar = vec3(0, 0, 0)
        self.center = vec3(0, 0, 0)
        self.eye = vec3(0, 0, 0)
        self.startX = 0
        self.startY = 0

        self.program = None
        self.mvp_id = 0
        self.vert_id = 0
        self.color_id = 0
        self.vertices = None

    def initializeGL(self):
        glClearColor(0, 0, 0, 1.0)
        glEnable(GL_DEPTH_TEST)

        vs = compileShader(self.vertexShader, GL_VERTEX_SHADER)
        fs = compileShader(self.fragmentShader, GL_FRAGMENT_SHADER)
        self.program = compileProgram(vs, fs)
        glUseProgram(self.program)

        self.mvp_id = glGetUniformLocation(self.program, 'MVP')
        self.vert_id = glGetAttribLocation(self.program, 'vert')
        self.color_id = glGetUniformLocation(self.program, 'fragmentColor')

        self.bindData()

    def paintGL(self):
        MVP = np.array(self.Projection() * self.View() * self.Model(), np.float32)

        # glUseProgram(self.program)

        # set uniforms
        glUniformMatrix4fv(self.mvp_id, 1, GL_FALSE, MVP)
        #
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #
        glUniform4f(self.color_id, 0.0, 1.0, 0.0, 1.0)

        glDrawArrays(GL_LINE_STRIP, 0, len(paralels_[0]))
        #


    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        # self.createProjectionMatrix(w, h)
        # self.bindmatrix()

    def Projection(self):
        near = 0.2
        far = 20
        angel = 45.0
        return perspective(radians(angel), 640/480, near, far)

    def View(self):
        up = vec3(0, -1, 0)
        return lookAt(self.eye, self.center, up)

    def Model(self):
        return mat4(1)

    def bindData(self):
        buffers = []
        vertexBuffer = glGenBuffers(len(paralels_[0]), buffers)
        print('WORKED!')
        glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
        vertexData = np.array(paralels_, np.float32)
        glBufferData(GL_ARRAY_BUFFER, 4 * len(vertexData), vertexData, GL_STATIC_DRAW)

        # enable attribute arrays
        glEnableVertexAttribArray(self.vert_id)
        # set vertex and UV buffers
        glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
        glVertexAttribPointer(self.vert_id, 3, GL_FLOAT, GL_FALSE, 0, None)

    def mousePressEvent(self, event):
        self.startX = event.pos().x()
        self.startY = event.pos().y()

    def mouseMoveEvent(self, event):
        self.center[0] = (event.pos().x() - self.startX) / 70
        self.center[1] = (self.startY - event.pos().y()) / 70
        print('move mouse')
        self.update()

    # def mouseReleaseEvent(self, event):
    #     x = event.pos().x()
    #     y = event.pos().y()
    #     print('release mouse', x, y)

    def keyPressed(self, key):
        p = self.polar
        s = 5
        if key == 87:
            p[0] += s
        if key == 83:
            p[0] -= s
        if key == 65:
            p[1] -= s
        if key == 68:
            p[1] += s
        print(p)
        self.toNormal(p[0], p[1])
        self.update()


    def toNormal(self, a, b):
        r = 3
        a *= np.pi / 180
        b *= np.pi / 180
        x = r * np.cos(a) * np.cos(b)
        y = r * np.sin(a)
        z = -r * np.cos(a) * np.sin(b)
        self.eye = vec3(x, y, z)
