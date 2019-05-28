#ifndef SPHERE_HPP
#define SPHERE_HPP
#include "Shape.hpp"
#include <glm/glm.hpp>
#include <vector>

class Sphere : public Shape {
private:
    glm::vec3 center;
    float radius;
    int sectors;
    int stack;
    bool movable = false;

    // std::vector<int>  indices;
    // std::vector<float>  points;
    // std::vector<float>  normals;
    std::vector<float>  norm_and_point;

public:
    Sphere (glm::vec3 center, float radius, int sectors, int stack, bool movable=false);
    ~Sphere (){};

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
