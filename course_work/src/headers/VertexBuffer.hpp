#ifndef VERTEXBUFFER_HPP
#define VERTEXBUFFER_HPP

#include <iostream>
class VertexBuffer {
private:
    unsigned int m_RendererID;

public:
    VertexBuffer (){};
    VertexBuffer (const void* data, unsigned int size);
    VertexBuffer& operator=(const VertexBuffer& other){
        std::cout << "assignment of \n";
        if (this != &other) {
            this->m_RendererID = other.m_RendererID;
        }
        return *this;
    }

    ~VertexBuffer ();
    void Bind() const;
    void Unbind() const;
};

#endif
