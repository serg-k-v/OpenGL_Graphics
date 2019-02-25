from OpenGL.GL import *
import numpy as np

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

def draw_line(width_line, color, beg_coord, end_coord, point_smooth):
    glLineWidth(width_line)
    glColor3d(color[0], color[1], color[2])
    glBegin(GL_LINES)
    glVertex3d(beg_coord[0], beg_coord[1], beg_coord[2])
    glVertex3d(end_coord[0], end_coord[1], end_coord[2])
    glEnd()

def draw_line_strip(width_line, color, beg_coord, end_coord, point_smooth, *addit_end_coord):
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

def gl_fill_t(filling_type) :
    if filling_type == 'fill' :
        return GL_FILL
    elif filling_type == 'line' :
        return GL_LINE
    elif filling_type == 'point' :
        return GL_POINT
    else :
        print("Error arguments!")

def draw_triangle(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_TRIANGLES)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw_triangle_strip(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_TRIANGLE_STRIP)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw_triangle_fan(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_TRIANGLE_FAN)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw_quad(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_QUADS)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw_quad_strip(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_QUAD_STRIP)
    glColor3d(color[0], color[1], color[2])
    for el in coord:
        glVertex3d(el[0], el[1], el[2])
    glEnd()

def draw_polygon(width_line, color, coord, point_smooth, filling_type) :
    glLineWidth(width_line)
    glPolygonMode(GL_FRONT_AND_BACK, gl_fill_t(filling_type))
    glBegin(GL_POLYGON)
    # glColor3d(color[0], color[1], color[2])
    k = 0
    coeff = 20
    for el in coord:
        glColor3d(np.abs(color[0] - (k//2)*coeff), np.abs(color[1] - (k//3)*coeff),
        np.abs(color[2] - (k//2)*coeff))
        glVertex3d(el[0], el[1], el[2])
        k+=1
    glEnd()
