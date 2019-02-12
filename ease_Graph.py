from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_point( size, color, point_coord, point_smooth ) :
    glPointSize(size)
    if point_smooth :
        glEnable(GL_POINT_SMOOTH)
    else :
        glDisable(GL_POINT_SMOOTH)
    glBegin(GL_POINTS)
    glColor3d(color[0], color[1], color[2])
    glVertex3d(point_coord[0], point_coord[1], point_coord[2])
    glEnd()
    return

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_point(5, [1, 0, 0], [4.1, 5, 0], False)

    glutSwapBuffers()

def Init_GL_Window( num_window, width, height) :
    glutInint((sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow("My First app on OpenGL")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMainLoop()



def main() :
    global window
    Init_GL_Window(0, 640,480);
    print('I do it')
    # draw_point(5, [1, 0, 0], [4.1, 6, 0], True)

if __name__ == '__main__' : main() # указываем что этот фаил является главным
