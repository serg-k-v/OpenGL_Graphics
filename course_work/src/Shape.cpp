#include "headers/Shape.hpp"

#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>
#include <cmath>



Circle::Circle (glm::vec3 center, float radius, int sectors, bool movable = false):Shape(){
    this->center = center;
    this->radius = radius;
    this->sectors = sectors;
    this->movable = movable;
}
// const Circle::std::vector<int> get_indices const {return indices;}
// const Circle::std::vector<float> get_points const {return points;}

void Circle::create_indices(){
    indices = std::vector<int>(3*sectors);
    for (size_t i = 0; i < sectors; i++) {
        indices[3*i] = 0;
        indices[3*i+1] = i+1;
        indices[3*i+2] = i+2 <= sectors ? i+2 : 1 ;
    }
}
void Circle::create_point(){
    for (size_t i = 0; i < 3; i++) {
        points.push_back(center[i]);
    }
    for (size_t i = 0; i < sectors; i++) {
        points.push_back(center[0] + radius * cos( i * 2 * M_PI / sectors ));
        points.push_back(center[1] + radius * sin( i * 2 * M_PI/ sectors ));
        points.push_back(center[2] + 0);
    }
}
