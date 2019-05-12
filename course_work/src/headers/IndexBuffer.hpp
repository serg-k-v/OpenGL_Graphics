#ifndef INDEXBUFFER_HPP
#define INDEXBUFFER_HPP

class IndexBuffer {
private:
    unsigned int m_RendererID;
    unsigned int m_Count;

public:
    IndexBuffer (const int* data, unsigned int count);
    ~IndexBuffer ();

    void Bind() const;
    void Unbind() const;
};

#endif
