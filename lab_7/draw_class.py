from OpenGL.GL import *
from OpenGL.GLUT import *
# import glm
import numpy as np
import Circle as crcl

width, height = 600,600

zoomFactor = 1.0
previous_m_state_x, previous_m_state_y = 0,0
mouse_speed = 1.5
horisontal_angle = np.pi
vertical_angle = 0.0

scalar_matrix = np.array([[zoomFactor, 0.0, 0.0, 0.0],
                          [0.0, zoomFactor, 0.0, 0.0],
                          [0.0, 0.0, zoomFactor, 0.0,],
                          [0.0, 0.0, 0.0, 1.0]])

view_matrix = np.array([[1.0, 0.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0, 0.0],
                        [0.0, 0.0, 1.0, 0.0],
                        [0.0, 0.0, 0.0, 1.0]])

rotate_mtr_on_z = lambda alpha : np.array([[np.cos(alpha),0,np.sin(alpha)], [0,1,0],[-np.sin(alpha),0,np.cos(alpha)]])

circle = crcl.Circle([0,0], 0.9, 100)
circle_coords = circle.create_shape()
print(circle_coords)

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

def mouse(button, state, x, y):
    global zoomFactor, scalar_matrix
    if button == 3 :
        if zoomFactor + 0.05 < 2 :
            zoomFactor += 0.05;
    elif button == 4:
        if zoomFactor - 0.05  > 0.4 :
            zoomFactor -= 0.05;
    scalar_matrix = np.array([[zoomFactor, 0.0, 0.0, 0.0],
                             [0.0, zoomFactor, 0.0,  0.0],
                             [0.0, 0.0, zoomFactor, 0.0,],
                             [0.0, 0.0, 0.0,        1.0]])
    # glutPostRedisplay() #for redraw

def draw():
    glClear(GL_COLOR_BUFFER_BIT)      # Очищаем экран и заливаем серым цветом
    glEnableClientState(GL_VERTEX_ARRAY) # Включаем использование массива вершин
    #
    # for arr_ in meredians_arr:
    #     glVertexPointer(3, GL_FLOAT, 0, arr_)
    #     glDrawArrays(GL_LINE_STRIP, 0, len(arr_))
    #
    # for arr_ in paralels_arr:
    #     glVertexPointer(3, GL_FLOAT, 0, arr_)
    #     glDrawArrays(GL_LINE_LOOP, 0, len(arr_))

    glVertexPointer(3, GL_FLOAT, 0, circle_coords)
    glDrawArrays(GL_TRIANGLE_FAN, 0, len(circle_coords))


    glDisableClientState(GL_VERTEX_ARRAY) # Отключаем использование массива вершин

    vertexShader = """

    void main(){
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex; //for gScalar
    }
    """
    fragmentShader = """
    void main() {
    	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0);
    }"""

    shader = create__shader(vertexShader, fragmentShader)
    glUseProgram(shader)

    modelMatIdx = glGetUniformLocation(shader, "modelMat")
    viewMatIdx = glGetUniformLocation(shader, "viewMat")
    # projMatIdx = glGetUniformLocation(shader, "projMat")
    global scalar_matrix, view_matrix

    glUniformMatrix4fv(modelMatIdx, 1, GL_FALSE, scalar_matrix);
    glUniformMatrix4fv(viewMatIdx, 1, GL_FALSE, view_matrix);
    # glUniformMatrix4fv(modelMatIdx, 1, FALSE_, glm.value_ptr(modelMat));

    glutSwapBuffers()   # Выводим все нарисованное в памяти на экран

#

def Init_GL_Window(num_window, width, height) :
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutInit(sys.argv)
    glutCreateWindow(b"Shaders!")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMouseFunc(mouse)

    glClearColor(0.2, 0.2, 0.2, 1)
    glRotatef(-40, 1, 0, 0)     # Поворот шейдера в нужную проекцию
    glRotatef(50, 0, 1, 0)

    glutMainLoop()


def main() :
    Init_GL_Window(0, width, height)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
