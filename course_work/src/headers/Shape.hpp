#ifndef HADER_HPP
#define HADER_HPP

class Shape {
private:

public:
    Shape (){}
    virtual ~Shape (){}
    virtual void create_point() = 0;
    virtual void create_indices() = 0;
    virtual void create_normals() = 0;
};

#endif
