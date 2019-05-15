#include "headers/Shader.hpp"
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

Shader::Shader(const std::string& filepath) :
        m_FilePath(filepath), m_RendererID(0){

    ShaderProgramSource sourse = ParseShader(filepath);
    m_RendererID = CreateShader(sourse.VertexSource, sourse.FragmentSourse);
}
Shader::~Shader (){
    glDeleteProgram(m_RendererID);
}

void Shader::Bind() {
    glUseProgram(m_RendererID);
}
void Shader::Unbind() {
    glUseProgram(0);
}

void Shader::SetUniform4f(const std::string& name, float v0, float v1, float v2, float v3) {
    glUniform4f(GetUniformLocation(name), v0, v1, v2, v3);
}

void Shader::SetMat4(const std::string &name, const glm::mat4 &mat){
    glUniformMatrix4fv(GetUniformLocation(name), 1, GL_FALSE, &mat[0][0]);
}

unsigned int Shader::CompileShader(unsigned int type, const std::string& sourse){
    unsigned int id = glCreateShader(type);
    const char* src = sourse.c_str();
    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    int result;
    glGetShaderiv(id, GL_COMPILE_STATUS, &result);
    if (result == GL_FALSE){
        int length;
        glGetShaderiv(id, GL_INFO_LOG_LENGTH, &length);
        char* message = (char*)alloca(length*sizeof(char));
        glGetShaderInfoLog(id, length, &length, message);
        std::cout << "Failed to compile " << (type == GL_VERTEX_SHADER ? "vertex" : "fragment") << '\n';
        std::cout << message << '\n';

        glDeleteShader(id);
        return 0;
    }
    return id;
}

unsigned int Shader::CreateShader(const std::string& vertexShader, const std::string& fragmentShader){
    unsigned int program = glCreateProgram();
    unsigned int vs = CompileShader(GL_VERTEX_SHADER, vertexShader);
    unsigned int fs = CompileShader(GL_FRAGMENT_SHADER, fragmentShader);

    glAttachShader(program, vs);
    glAttachShader(program, fs);

    glLinkProgram(program);
    glValidateProgram(program);

    glDeleteShader(vs);
    glDeleteShader(fs);

    return program;
}

ShaderProgramSource Shader::ParseShader(const std::string& filepath){
    std::ifstream stream(filepath);

    if(!stream.is_open()){
        std::cout << "Straem dosn't open!" << '\n';
    }

    enum class ShaderType {
        NONE = -1, VERTEX = 0, FRAGMENT = 1
    };
    std::string line;
    std::stringstream ss[2];
    ShaderType type =  ShaderType::NONE;
    while (getline(stream, line)) {
        if (line.find("#shader") != std::string::npos){
            if (line.find("vertex") != std::string::npos)
                type = ShaderType::VERTEX;
            else if (line.find("fragment") != std::string::npos)
                type = ShaderType::FRAGMENT;
        } else {
            ss[(int)type] << line << '\n';
        }
    }

    // std::cout << "Shader : " << ss[0].str() << '\n' << ss[1].str() << '\n';
    return {ss[0].str(), ss[1].str()};
}

unsigned int Shader::GetUniformLocation(const std::string& name){
    int location = glGetUniformLocation(m_RendererID, name.c_str());
    if (location == -1)
        std::cout << "Warning : uniform " << name << " dosn't exist!" << '\n';
    return location;
}
