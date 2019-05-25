#include "headers/Torus.hpp"
#include "headers/Circle.hpp"

#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>


Torus::Torus (glm::vec3 center, float sircl_radius, int sectors, float torus_radius, bool movable):Shape() {
    this->center = center;
    this->sircl_radius = sircl_radius;
    this->sectors = sectors;
    this->torus_radius = torus_radius;
    this->movable = movable;
    try{
        this->circle = new Circle(center+glm::vec3(torus_radius, 0, 0), sircl_radius, sectors);
    }catch(const std::bad_alloc& e){
        std::cout << "Allocation failed: " << e.what() << '\n';
    }
}

void Torus::create_indices() {
    // for (size_t i = 0; i < (size_t)sectors; i++) {
    //     indices.push_back(0);
    //     indices.push_back(i+1);
    //     indices.push_back(i+2 <= (size_t)sectors ? i+2 : 1) ;
    // }
}
void Torus::create_point() {
    for (size_t i = 0; i < (size_t)sectors; i++) {
        points.push_back(center[0] + radius * glm::cos( i * 2 * glm::pi<float>() / sectors));
        points.push_back(center[2] + 0);
        points.push_back(center[1] + radius * glm::sin( i * 2 * glm::pi<float>() / sectors));
    }
}

void Torus::create_normals() {
    // glm::vec3 v1(points[3], points[4], points[5]);
    // glm::vec3 v2(points[6], points[7], points[8]);
    // glm::vec3 res = glm::normalize(glm::cross(v1 - center, v2 - center));
    // for (size_t i = 0; i < 3; i++) {
    //     normals.push_back(res[i]);
    // }
}
