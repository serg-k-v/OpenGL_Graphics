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

def draw_line(width_line, color, beg_coord, end_coord, point_smooth) :
    glLineWidth(width_line)
    glColor3d(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex3d(beg_coord[0], beg_coord[1], beg_coord[2])
    glVertex3d(end_coord[0], end_coord[1], end_coord[2])
    glEnd()

def draw_line_strip(width_line, color, beg_coord, end_coord, point_smooth, *addit_end_coord) :
    glLineWidth(width_line)
    glBegin(GL_LINE_STRIP)
    # base line
    glColor3d(color[0], color[1], color[2])
    glVertex3d(beg_coord[0], beg_coord[1], beg_coord[2])
    glVertex3d(end_coord[0], end_coord[1], end_coord[2])
    # addition line
    for coord  in addit_end_coord:
        glColor3d(0, 1, 0)
        glVertex3d(coord[0], coord[1], coord[2])
    glEnd()

def draw_line_loop(width_line, color, beg_coord, end_coord, point_smooth, *addit_end_coord) :
    glLineWidth(width_line)
    glBegin(GL_LINE_LOOP)
    # base line
    glColor3d(color[0], color[1], color[2])
    glVertex3d(beg_coord[0], beg_coord[1], beg_coord[2])
    glVertex3d(end_coord[0], end_coord[1], end_coord[2])
    # addition line
    for coord  in addit_end_coord:
        glColor3d(0, 1, 0)
        glVertex3d(coord[0], coord[1], coord[2])
    glEnd()
    pass

def draw_triangles(width_line, color, coord, point_smooth, tr_type) :
    glLineWidth(width_line)
    print(GL_TRIANGLES)
    if tr_type == 'fill' :
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    elif tr_type == 'line' :
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    elif tr_type == 'point' :
        glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
    else :
        print("Error arguments!")
    glBegin(GL_TRIANGLES)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_point(10, [.1, .1, .5], [100, 200, 0], False)
    draw_point(20, [.1, .17, .5], [50, 100, 0], False)
    draw_point(40, [.3, .5, 0.5], [150, 400, 0], True)

    draw_line(5, [1., .5, 1.], [50, 50, 0], [300, 100, 0], False)
    draw_line(5, [1., 1., 1.], [300, 50, 0], [500, 400, 0], False)

    draw_line_strip(20, [1, 0, 0], [50, 200, 0], [200, 350, 0], False,
    [250, 550,0], [400, 380,0], [150, 60, 0])

    draw_line_loop(20, [0, 1, 0.9], [0, 220, 0], [180, 380, 0], False,
    [290, 590,0], [420, 390,0], [190, 130, 0])

    draw_triangles(15, [0.2, 0.3, 0.8], [[500, 500, 0],[20, 20, 0],[600, 20, 0]], False, 'fill')

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
