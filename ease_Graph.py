from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_point( size, color, point_coord, point_smooth ) :
    glPointSize(size)
    glColor3d(color[0], color[1], color[2])
    if point_smooth :
        glEnable(GL_POINT_SMOOTH)
    else :
        glDisable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex3d(point_coord[0], point_coord[1], point_coord[2])
    glEnd()
    return

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    refresh2d(640, 480)
    draw_point(400, [1.0, 1.0, 0], [10, 20, 0], False)
    glutSwapBuffers()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)


def Init_GL_Window(num_window, width, height) :
    global window # must be around glutCreateWindow
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(300, 300)

    window = glutCreateWindow("My First app on OpenGL")

    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()



def main() :
    Init_GL_Window(0, 640,480);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
