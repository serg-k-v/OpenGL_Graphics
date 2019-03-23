
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
        length =glGetShaderiv(id, GL_INFO_LOG_LENGTH)
        info = glGetShaderInfoLog(id)
        print('error ! : ', info)
        glDeleteShader(id)
        return 'PIZDA'
    return id

def create__shader(vertexShader, fragmentShader) :
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vertexShader)
    fs = compile_shader(GL_FRAGMENT_SHADER, fragmentShader)
    print('FUCK', fs)
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)
    glValidateProgram(program)
    glDeleteShader(vs)
    glDeleteShader(fs)

    return program

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # position = np.array([[-1/2, 1/2, 0],[1/2, 1/2, 0],[1/2, -1/2, 0],[-1/2, -1/2, 0]], dtype='float32')
    # position = np.array(
    # [-1/2, 1/2, 0,
    #   1/2, 1/2, 0,
    #   1/2, -1/2, 0,
    #   -1/2, -1/2, 0 ], dtype='float32')
    position = np.array(
    [-1/2, -1/2,
      0, 1/2,
      1/2, -1/2], dtype='float32')

    # buffer = glGenBuffers(1)
    # glBindBuffer(GL_ARRAY_BUFFER, buffer)
    # glBufferData(GL_ARRAY_BUFFER, position.itemsize*len(position), position, GL_STATIC_DRAW)
    #
    # glEnableVertexAttribArray(0)
    # glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, position.itemsize*2, 0)
    #
    # glBindBuffer(GL_ARRAY_BUFFER, 0)



    vertexShader = """
    #version 450 core
    in vec4 position;

    void main() {
         gl_Position = position;
    }
    """

    fragmentShader = """
    #version 450 core
    out vec4 color;

    void main() {
        color = vec4(1.0, 0.0, 0.0, 1.0);
    }
    """
    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader);
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glutSwapBuffers()



def Init_GL_Window(num_window, width, height) :
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(300, 300)
    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    # glClearColor(.6, .2, .4 , 1.0) # background color
    glutInitContextProfile(GLUT_CORE_PROFILE)
    glutInitContextVersion(4, 5)

    glutMainLoop()


def main() :
    Init_GL_Window(0, width, height);

if __name__ == '__main__' : main() # указываем что этот фаил является главным
