#ifndef HADER_HPP
#define HADER_HPP

#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>
#include <cmath>

class Shape {
private:

public:
    Shape (){}
    virtual ~Shape (){}
    virtual void create_point() = 0;
    virtual void create_indices() = 0;
};

class Circle : public Shape {
private:
    glm::vec3 center;
    float radius;
    int sectors;
    bool movable = false;

    std::vector<int>  indices;
    std::vector<float>  points;

public:
    Circle (glm::vec3 center, float radius, int sectors, bool movable=false);
    const std::vector<int> get_indices() const {return indices;}
    const std::vector<float> get_points() const {return points;}
    void create_indices();
    void create_point();

};

#endif
