#include "headers/Cylinder.hpp"
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <glm/gtc/type_ptr.hpp>
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

    create_point();
    create_indices();
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

Cylinder::~Cylinder() {
    delete circle;
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
    for (size_t i = 0; i < points.size()/3; i++) {
        glm::vec3 v(points[3*i],   points[3*i+1],   points[3*i+2]);
        glm::vec3 res = v - center;
        normals.insert(normals.end(), glm::value_ptr(res), glm::value_ptr(res)+3);
    }
}

void Cylinder::join_data() {
    auto points_it = points.begin();
    auto normals_it = normals.begin();
    for (size_t i = 0; i < points.size()/3; i++) {
        norm_and_point.insert(norm_and_point.end(), points_it, points_it+3);
        norm_and_point.insert(norm_and_point.end(), normals_it, normals_it+3);
        points_it+=3;
        normals_it+=3;
    }
}
