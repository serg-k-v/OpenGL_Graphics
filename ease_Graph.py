from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height = 640,480

def draw_point( size, color, point_coord, point_smooth ) :
    glPointSize(size)
    glColor3d(color[0], color[1], color[2])
    if point_smooth :
        glEnable(GL_POINT_SMOOTH)
    else :
        glDisable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glVertex3d(point_coord[0], point_coord[1], point_coord[2])
    glVertex3d(point_coord[0], point_coord[1], point_coord[2])
    glEnd()



def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_point(10, [.1, .1, .5], [100, 200, 0], False)
    draw_point(20, [.1, .17, .5], [50, 100, 0], False)
    draw_point(40, [.3, .5, 0.5], [150, 400, 0], False)

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
    glClearColor(.26, .23, .51 , 1.0) # background color
    glutMainLoop()



def main() :
    Init_GL_Window(0, width, height);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
