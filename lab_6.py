# -*- coding: utf-8 -*-
# Импортируем все необходимые библиотеки:
from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
# Из модуля random импортируем одноименную функцию random
from random import random
import numpy as np
import matplotlib.pyplot as plt
# объявляем массив pointcolor глобальным (будет доступен во всей программе)
global pointcolor

width, height = 600,600

data = np.array([[108.1, 234, 0],
                [91.1, 232.8, 0],
                [75.5, 229, 0],
                [64.1, 224.1, 0],
                [48.2, 210.5, 0],
                [44.4, 194.2, 0],
                [47.9, 179.1, 0],
                [59.3, 171.2, 0],
                [65, 175.7, 0],
                [70.1, 182.3, 0],
                [79.7, 183.3, 0],
                [88.2, 181.3, 0],
                [92.9, 175.9, 0],
                [91.5, 166.3, 0],
                [86, 156.9, 0],
                [74, 139.5, 0],
                [66.7, 123.7, 0],
                [64.6, 114.7, 0],
                [65.4, 104.5, 0],
                [77.5, 92.2, 0],
                [98.3, 89, 0],
                [108.1, 88.8, 0]])
max_y = max(data[:,1])
max_x = max(data[:,0])
for i in range(len(data)):
    data[i] = [(data[i][0] - max_x)/max_x, (data[i][1] - max_y/2)/max_y*1.7, 0]

rotate_mtr_on_z = lambda alpha : np.array([[np.cos(alpha),0,np.sin(alpha)], [0,1,0],[-np.sin(alpha),0,np.cos(alpha)]])

def create_greed(points) :
    global data
    n = int(360/10)
    for i in range(1,n+1):
        alpha = (i)*(2*np.pi/n)
        print('alpha : ', alpha)
        tmp = points.dot(rotate_mtr_on_z(alpha))
        # print("tmp data : ", data)
        data = np.concatenate((data, tmp))

def addition_greed(points, size_one_line) :
    arr = np.empty((len(points),3))
    i = 0
    print('len : ', len(data))
    while len(data) > i:
        arr[i] = points[i]
        arr[i+1] = points[i*size_one_line]
    return arr


len_data = len(data)
create_greed(data)
# print('data : \n', data)

# print(pointdata)
pointdata = data

print('result : \n', pointdata)


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
    glClear(GL_COLOR_BUFFER_BIT)                    # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)            # Включаем использование массива вершин
    # glEnableClientState(GL_COLOR_ARRAY)
    # glColorPointer(3, GL_FLOAT, 0, pointcolor)
    # print(pointdata)
    glVertexPointer(3, GL_FLOAT, 0, pointdata)
    glDrawArrays(GL_LINE_STRIP, 0, len(pointdata))

    glDisableClientState(GL_VERTEX_ARRAY)           # Отключаем использование массива вершин
    # glDisableClientState(GL_COLOR_ARRAY)            # Отключаем использование массива цветов

    vertexShader = """
    //uniform float Time;
    //uniform float  K;
    //uniform float Velocity;
    //uniform float Amp;
    //uniform mat3 NormalMatrix;
    //uniform mat4 MVP;

    void main(){
        //out vec4 Position;
        //out vec3 Normal;

        //vec4 pos = vec4(vec3(), 1.0);
        //pos.y = Amp * sin( K * (pos.x - Velocity * Time) );

        //vec3 n = vec3(0.0);
        //n.xy = normalize(vec2(-K * Amp * cos(u), 1.0));

        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
        //Normal = NormalMatrix * n;
    }
    """
    fragmentShader = """
    void main() {
    	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0);
    }"""

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)

    # time = (glutGet(GLUT_ELAPSED_TIME)/1000.)
    # K = 10.0
    # Velocity = 1.0
    # Amp = 0.13
    #
    # uniforms = {
    #     'time': glGetUniformLocation(shader, 'Time'),
    #     'K': glGetUniformLocation(shader, 'K'),
    #     'Velocity': glGetUniformLocation(shader, 'Velocity'),
    #     'Amp': glGetUniformLocation(shader, 'Amp'),
    #     }
    # glUniform1f(uniforms['time'], time)
    # glUniform1f(uniforms['K'], K)
    # glUniform1f(uniforms['Velocity'], Velocity)
    # glUniform1f(uniforms['Amp'], Amp)


    glutSwapBuffers()                               # Выводим все нарисованное в памяти на экран

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
