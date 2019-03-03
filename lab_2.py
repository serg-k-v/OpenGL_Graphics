from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from gl_implement import gl_primitives as prm

width, height = 640,480

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # prm.draw_triangle(15, [0.2, 0.3, 0.8], [[500, 500, 0],[450, 20, 0],
    # [600, 20, 0]], False, 'fill')
    # prm.draw_triangle_fan(50, [.4, 0.2, 0.7], [[420, 600, 0],[30, 510, 0],
    # [70, 70, 0],[250, 250, 0]],  False, 'line')
    # prm.draw_triangle_strip(10, [.5, 0.1, 0.6], [[420, 600, 0],[30, 510, 0],
    # [70, 70, 0],[250, 250, 0]],  False, 'line')
    #
    # prm.draw_quad(30, [0.1, 0.8, 0.2], [[500, 500, 0],[580, 500, 0],
    # [600, 20, 0],[450, 20, 0]], False, 'line')
    # prm.draw_quad_strip(30, [0.9, 0.5, 0.2], [[500, 500, 0],[460, 500, 0],
    # [600, 20, 0],[280, 280, 0],[450, 20, 0], [40, 70, 0]], False, 'line')

    coord = [[50, 300, 0],[150, 250, 0],[400, 550, 0],[450,320,0],
    [100, 100, 0],[200, 280, 0], [100, 50, 0]]

    choise = 'blend'
    # choise = 'alpha'

    if choise == 'cat' :
        parametr = GL_SCISSOR_TEST
        glScissor(200,200,100,80) # begin point, width and height
    elif choise == 'alpha' :
        parametr = GL_ALPHA_TEST
        glAlphaFunc(GL_GREATER,0.4)
    elif choise == 'blend' :
        parametr = GL_BLEND
        sfactor = GL_SRC_ALPHA
        dfactor = GL_ONE_MINUS_SRC_ALPHA
        glBlendFunc(sfactor,dfactor) #???

    glEnable(parametr)
    # prm.draw_polygon(15, [255, 0, 240], coord , False, 'fill')
    glBegin(GL_POLYGON)
    glColor4d(0.1, 0, 0, .4)
    glVertex3d(50, 300, 0)
    # glColor4d(0.8, 0.5, 0.1)
    glVertex3d(150, 250, 0)
    # glColor4d(0.2, 0.5, 0.7)
    glVertex3d(400, 550, 0)
    glColor4d(0.4, 0.5, 0.9, .8)
    glVertex3d(450,320,0)
    glColor4d(0.9, 0, 0, .2)
    glVertex3d(100, 100, 0)
    # glColor4d(0.6, 0.8, 0.6)
    glVertex3d(200, 280, 0)
    glColor4d(0.9, 0.5, 0.6, .5)
    glVertex3d(100, 50, 0)
    glEnd()
    glDisable(parametr);

    glutSwapBuffers()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, -1.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glutPostRedisplay()

def Init_GL_Window(num_window, width, height) :

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(300, 300)

    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    # glutIdleFunc(draw)
    glutReshapeFunc(refresh2d)
    glClearColor(.6, .2, .4 , 1.0) # background color
    glutMainLoop()

def main() :
    Init_GL_Window(0, width, height);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
