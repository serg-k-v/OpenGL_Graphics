# -*- coding: utf-8 -*-
# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
import numpy as np
import bezier_curves as b_c

width, height = 600,600

rotate_mtr_on_z = lambda alpha : np.array([[np.cos(alpha),0,np.sin(alpha)], [0,1,0],[-np.sin(alpha),0,np.cos(alpha)]])

def make_copy(points) :
    n = int(360/20)
    arr_points = np.empty((n,len(data),3))
    for i in range(0,n):
        alpha = (i+1)*(2*np.pi/n)
        tmp = points.dot(rotate_mtr_on_z(alpha))
        arr_points[i] = tmp
    return arr_points

def paralels(points) :
    return points.transpose((1,0,2))

data = b_c.get_data()
tmp = np.insert(data, 2, 0, axis=1)
max_y = max(tmp[:,1])
max_x = max(tmp[:,0])
for i in range(len(tmp)):
    tmp[i] = [(tmp[i][0] - max_x)/max_x, (tmp[i][1] - max_y/2)/max_y*1.7, 0]

meredians_arr = make_copy(tmp)
paralels_arr  = paralels(meredians_arr)


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
        return None
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

def draw():
    glClear(GL_COLOR_BUFFER_BIT)      # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY) # Включаем использование массива вершин

    for arr_ in meredians_arr:
        glVertexPointer(3, GL_FLOAT, 0, arr_)
        glDrawArrays(GL_LINE_STRIP, 0, len(arr_))

    for arr_ in paralels_arr:
        glVertexPointer(3, GL_FLOAT, 0, arr_)
        glDrawArrays(GL_LINE_LOOP, 0, len(arr_))

    glDisableClientState(GL_VERTEX_ARRAY) # Отключаем использование массива вершин

    vertexShader = """
    void main(){
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }
    """
    fragmentShader = """
    void main() {
    	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0);
    }"""

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)
    glutSwapBuffers()   # Выводим все нарисованное в памяти на экран

def Init_GL_Window(num_window, width, height) :
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutInit(sys.argv)
    glutCreateWindow(b"Shaders!")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glClearColor(0.2, 0.2, 0.2, 1)
    #
    glRotatef(-10, 1, 0, 0)     # Поворот шейдера в нужную проекцию
    glRotatef(60, 0, 1, 0)
    glRotatef(40, 0, 0, 1)

    glutMainLoop()


def main() :
    Init_GL_Window(0, width, height)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
