#ifndef CYLINDER_HPP
#define CYLINDER_HPP

#include <glm/glm.hpp>
#include <vector>
#include "Circle.hpp"
#include "Shape.hpp"


class Cylinder : public Shape {
private:
    // glm::vec3 center;
    float radius;
    float height;
    int sectors;
    bool movable;

    Circle* circle;
    // std::vector<int>  indices;
    // std::vector<float>  points;
    // std::vector<float>  normals;
    std::vector<float>  norm_and_point;

public:
    Cylinder (glm::vec3 center, float radius, float height, int sectors, bool movable=false);
    ~Cylinder();
    // const std::vector<int> &get_indices() const {return indices;}
    // const std::vector<float> &get_points() const {return points;}
    // const std::vector<float> &get_normals() const {return normals;}
    const std::vector<float> &get_n_p() const {return norm_and_point;}
    void create_indices();
    void create_point();
    void create_normals();
    void join_data();
};

#endif
