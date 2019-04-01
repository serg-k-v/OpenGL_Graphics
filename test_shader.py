
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from gl_implement import gl_primitives as prm

width, height = 640,480


def compile_shader(type, sourse) :
    id = glCreateShader(type)
    glShaderSource(id, sourse)
    glCompileShader(id)

    result = glGetShaderiv(id, GL_COMPILE_STATUS)
    if result == GL_FALSE :
        length = glGetShaderiv(id, GL_INFO_LOG_LENGTH)
        info = glGetShaderInfoLog(id)
        print('error ! : ', info)
        glDeleteShader(id)
        return 'PIZDA'
    return id

def create__shader(vertexShader, fragmentShader) :
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vertexShader)
    fs = compile_shader(GL_FRAGMENT_SHADER, fragmentShader)

    glAttachShader(program, vs)
    glAttachShader(program, fs)

    glLinkProgram(program)
    glValidateProgram(program)
    glDeleteShader(vs)
    glDeleteShader(fs)

    return program

def draw() :
    glClear(GL_COLOR_BUFFER_BIT)
    # glLoadIdentity()
    # position = np.array([[-1/2, 1/2, 0],[1/2, 1/2, 0],[1/2, -1/2, 0],[-1/2, -1/2, 0]], dtype='float32')

    position = np.array( [-0.5, -0.5, 0, 0.5, 0.5, -0.5], dtype='float32')

    glEnableClientState(GL_VERTEX_ARRAY)
    # glEnableClientState(GL_COLOR_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, position)
    # glColorPointer(3, GL_FLOAT, 0, pointcolor)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glDisableClientState(GL_VERTEX_ARRAY)
    # glDisableClientState(GL_COLOR_ARRAY)            # Отключаем использование массива вершин
    glutSwapBuffers()


def g___g() :
        vertexShader = """
        void main() {
             gl_Position = gl_Vertex;
        }
        """

        fragmentShader = """
        varying vec4 vertex_color;
                    void main() {
                        gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
        }"""
        shader = create__shader(vertexShader, fragmentShader)
        glUseProgram(shader);

def Init_GL_Window(num_window, width, height) :
    glutInit()

    glutInitContextVersion(4, 5);
    glutInitContextFlags(GLUT_FORWARD_COMPATIBLE);
    glutInitContextProfile(GLUT_CORE_PROFILE);


    glutInitWindowSize(width, height)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowPosition(300, 300)
    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    # glClearColor(.6, .2, .4 , 1.0) # background color
    g___g()
    glutMainLoop()


def main() :
    Init_GL_Window(0, width, height);

if __name__ == '__main__' : main() # указываем что этот фаил является главным
