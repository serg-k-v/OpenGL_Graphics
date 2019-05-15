#include "headers/Cylinder.hpp"
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>
// #include <typeinfo>

Cylinder::Cylinder (glm::vec3 center, float radius, float height, int sectors, bool movable):Shape() {
    this->center = center;
    this->radius = radius;
    this->height = height;
    this->sectors = sectors;
    this->movable = movable;
    try{
        this->circle = new Circle(center, radius, sectors);
    }catch(const std::bad_alloc& e){
        std::cout << "Allocation failed: " << e.what() << '\n';
    }

}

void Cylinder::create_indices() {
    for (size_t i = 0; i < (size_t)sectors; i++) {
        for (size_t j = 1; j < 3; j++) {
            indices.push_back(i*2);
            indices.push_back((i*2+j) % (sectors*2));
            indices.push_back((i*2+3) % (sectors*2)) ;
        }
    }
}
void Cylinder::create_point() {
    circle->create_point();
    std::vector<float> tmp(circle->get_points());
    for (size_t i = 1; i < (size_t)sectors+1; i++) {

        // std::cout << "y+ = " << tmp[3*i+1] << '\n';
        points.push_back(tmp[3*i]);
        points.push_back(tmp[3*i+1]+height/2);
        points.push_back(tmp[3*i+2]);

        // std::cout << "y- = " << tmp[3*i+1]-height/2  << '\n';
        points.push_back(tmp[3*i]);
        points.push_back(tmp[3*i+1]-height/2);
        points.push_back(tmp[3*i+2]);
    }

}

void Cylinder::create_normals() {
    // circle->create_normals();
    // glm::vec3 v1(points[3], points[4], points[5]);
    // glm::vec3 v2(points[6], points[7], points[8]);
    // glm::vec3 res = glm::normalize(glm::cross(v1 - center, v2 - center));
    // for (size_t i = 0; i < 3; i++) {
    //     normals.push_back(res[i]);
    // }
}
