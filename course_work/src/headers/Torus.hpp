#ifndef TORUS_HPP
#define TORUS_HPP

#include <glm/glm.hpp>
#include <vector>
#include "Circle.hpp"
#include "Shape.hpp"


class Torus : public Shape {
private:
    // glm::vec3 center;
    float sircl_radius;
    int   sirc_sectors;
    float torus_radius;
    int   tor_sectors;
    bool  half    = false;
    bool  movable = false;

    Circle* circle;
    // std::vector<int>    indices;
    // std::vector<float>  points;
    // std::vector<float>  normals;
    // std::vector<float>  norm_and_point;

public:
    Torus (float sircl_radius, int sirc_sectors,
                             float torus_radius, float tor_sectors,
                             glm::vec3 center = glm::vec3(0, 0, 0),
                             glm::vec3 color = glm::vec3(1, 0.5, 0.2),
                             bool half =false, bool movable=false);
    ~Torus (){};

    // const std::vector<int> &get_indices() const {return indices;}
    // const std::vector<float> &get_points() const {return points;}
    // const std::vector<float> &get_normals() const {return normals;}
    const std::vector<float> &get_n_p() const {return norm_and_point;}
    void create_indices();
    void create_point();
    void create_normals();
    // void join_data();
};

#endif
