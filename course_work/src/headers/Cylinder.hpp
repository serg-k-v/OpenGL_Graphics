#ifndef CYLINDER_HPP
#define CYLINDER_HPP

#include <glm/glm.hpp>
#include <vector>
#include "Circle.hpp"
#include "Shape.hpp"


class Cylinder : public Shape {
private:
    glm::vec3 center;
    float radius;
    float height;
    int sectors;
    bool movable = false;

    Circle* circle;
    std::vector<int>  indices;
    std::vector<float>  points;
    std::vector<float>  normals;

public:
    Cylinder (glm::vec3 center, float radius, float height, int sectors, bool movable=false);
    const std::vector<int> &get_indices() const {return indices;}
    const std::vector<float> &get_points() const {return points;}
    const std::vector<float> &get_normals() const {return normals;}
    void create_indices();
    void create_point();
    void create_normals();
};

#endif
