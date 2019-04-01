from OpenGL.GL import *
from OpenGL.GLUT import *
#import sys
# Из модуля random импортируем одноименную функцию random
from random import random
from scipy.interpolate import lagrange
# объявляем массив pointcolor глобальным (будет доступен во всей программе)
global pointcolor


# Серый, тут задаем точки, по которым строим нашу кривую
def Lagrange(x, y, t):
    L = lagrange(x, y)
    y = L(t)
    return y

# Серый, начальные точки для Лагранжа
x = [i / 100 for i in range(-1000, 1000, 25)]
y = [-0.1, 0.1] * (len(x) // 2)

# Серый, точки, по которым строим кривую
t = [i / 100 for i in range(-90, 90, 1)]
z = [-0.80, 0.80] * len(t)
y = Lagrange(x, y, t)



# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    # Сообщаем о необходимости использовать глобального массива pointcolor
    global pointcolor
    # Обработчики специальных клавиш
    if key == GLUT_KEY_UP:          # Клавиша вверх
        glRotatef(5, 1, 0, 0)       # Вращаем на 5 градусов по оси X
    if key == GLUT_KEY_DOWN:        # Клавиша вниз
        glRotatef(-5, 1, 0, 0)      # Вращаем на -5 градусов по оси X
    if key == GLUT_KEY_LEFT:        # Клавиша влево
        glRotatef(5, 0, 1, 0)       # Вращаем на 5 градусов по оси Y
    if key == GLUT_KEY_RIGHT:       # Клавиша вправо
        glRotatef(-5, 0, 1, 0)      # Вращаем на -5 градусов по оси Y
    if key == GLUT_KEY_END:         # Клавиша END
        # Заполняем массив pointcolor случайными числами в диапазоне 0-1
        pointcolor = [[random(), random(), random()], [random(), random(), random()], [random(), random(), random()]]


# Процедура подготовки шейдера (тип шейдера, текст шейдера)
def create_shader(shader_type, source):
    # Создаем пустой объект шейдера
    shader = glCreateShader(shader_type)
    # Привязываем текст шейдера к пустому объекту шейдера
    glShaderSource(shader, source)
    # Компилируем шейдер
    glCompileShader(shader)
    # Возвращаем созданный шейдер
    return shader


def draw():
    glClear(GL_COLOR_BUFFER_BIT)                    # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY)            # Включаем использование массива вершин
    glEnableClientState(GL_COLOR_ARRAY)             # Включаем использование массива цветов

    glVertexPointer(3, GL_FLOAT, 0, pointdata)

    glColorPointer(3, GL_FLOAT, 0, pointcolor)

    glDrawArrays(GL_QUAD_STRIP, 0, len(pointdata))
    glDisableClientState(GL_VERTEX_ARRAY)           # Отключаем использование массива вершин
    glDisableClientState(GL_COLOR_ARRAY)            # Отключаем использование массива цветов

    vertex = create_shader(GL_VERTEX_SHADER, """
    varying vec4 vertex_color;
                void main(){
                    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                    vertex_color = gl_Color;
                }""")
    # Создаем фрагментный шейдер:
    # Определяет цвет каждого фрагмента как "смешанный" цвет его вершин
    fragment = create_shader(GL_FRAGMENT_SHADER, """
    varying vec4 vertex_color;
                void main() {
                    gl_FragColor = vertex_color;
    }""")
    # Создаем пустой объект шейдерной программы
    program = glCreateProgram()
    # Приcоединяем вершинный шейдер к программе
    glAttachShader(program, vertex)
    # Присоединяем фрагментный шейдер к программе
    glAttachShader(program, fragment)
    # "Собираем" шейдерную программу
    glLinkProgram(program)
    # Сообщаем OpenGL о необходимости использовать данную шейдерну программу при отрисовке объектов
    glUseProgram(program)
    glutSwapBuffers()                               # Выводим все нарисованное в памяти на экран


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(300, 300)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Shaders!")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glRotatef(-20, 1, 0, 0)     # Поворот шейдера в нужную проекцию
glRotatef(10, 0, 1, 0)      # То же
glClearColor(0.2, 0.2, 0.2, 1)

# Создаем вершинный шейдер:
# Положение вершин не меняется
# Цвет вершины - такой же как и в массиве цветов


# Задаем массив точек, по которым будем делать шейдер
pointdata = [[t[i // 2 + i % 2], y[i // 2 + i % 2], z[i]] for i in range(0, len(z) - 1)]
print(pointdata)

pointcolor = [[i % 2, i % 2, i % 2] for i in range(0, len(z) - 1)]
glutMainLoop()
