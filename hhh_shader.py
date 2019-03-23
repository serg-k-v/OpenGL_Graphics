# import numpy as np
import sys


def compile_shader(sourse, type) :
    id = glCreateShader(GL_VERTEX_SHADER)
    glShaderSourse(id, sourse)
    glCompileShader(id)

    result = glGetShaderiv(id, GL_COMPILE_STATUS)
    if result == GL_FALSE :
        print('that\'s a sheet')
        glDeleteShader(id)
        return

    return id;

def create_vertex_shader(vertexShader) :
    program = glCreateProgram()
    vs = compile_shader(GL_VERTEX_SHADER, vertexShader)

    glAttachShader(program)
    glLinkProgram(program)
    glValidateProgram(program)

    glDeleteShader(vs)

    return program

def main() :
    vertexShader = """ #version 400
    layout(location = 0) in vec4 position;

    void main() {
         gl_Position = position
    }"""

    shader = create_vertex_shader(vertexShader)
    glUseProgram(shader);

    position = [[-1/2, 1/2, 0],[1/2, 1/2, 0],[1/2, -1/2, 0],[-1/2, -1/2, 0]]

    buffer = Gluint(position)
    glGEnBuffers(1, buffer)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    glBufferData(GL_ARRAY_BUFFER, sys.getsizeof(position), position[0] ,GL_STATIC_DRAW)

    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, ,0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)



if __name__ == '__main__':
    main()
