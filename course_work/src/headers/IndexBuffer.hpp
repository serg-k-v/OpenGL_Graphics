#ifndef INDEXBUFFER_HPP
#define INDEXBUFFER_HPP

class IndexBuffer {
private:
    unsigned int m_RendererID;
    unsigned int m_Count;

public:
    IndexBuffer (){};
    IndexBuffer (const int* data, unsigned int count);
    IndexBuffer& operator=(const IndexBuffer& other){
        std::cout << "assignment of \n";
        if (this != &other) {
            this->m_RendererID = other.m_RendererID;
            this->m_Count = other.m_Count;
        }
        return *this;
    }
    ~IndexBuffer ();

    void Bind() const;
    void Unbind() const;
};

#endif
