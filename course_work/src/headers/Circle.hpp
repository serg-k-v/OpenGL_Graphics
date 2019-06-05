#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include <glm/glm.hpp>
#include <vector>
#include "Shape.hpp"


class Circle : public Shape {
private:
    // glm::vec3 center;
    float radius;
    int sectors;
    bool movable = false;

    // std::vector<int>  indices;
    // std::vector<float>  points;
    // std::vector<float>  normals;

public:
    Circle (float radius, int sectors,
            glm::vec3 center = glm::vec3(0, 0, 0),
            glm::vec3 color = glm::vec3(1, 0.5, 0.2), bool movable=false);
    // const std::vector<int> get_indices() const {return indices;}
    // const std::vector<float> get_points() const {return points;}
    // const std::vector<float> get_normals() const {return normals;}
    void create_indices();
    void create_point();
    void create_normals();
};

#endif
