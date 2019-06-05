#include "headers/Cylinder.hpp"
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <vector>
#include <iostream>
// #include <typeinfo>

Cylinder::Cylinder (float radius, float height, int sectors,
                    glm::vec3 center, glm::vec3 color,
                    bool movable):Shape(center, color){
    // this->center = center;
    this->radius = radius;
    this->height = height;
    this->sectors = sectors;
    this->movable = movable;
    try{
        this->circle = new Circle(radius, sectors, center, color);
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

    for (size_t i = 0; i < (size_t)sectors*2; i+=2) {
        indices.push_back(i);
        indices.push_back(sectors*2);
        indices.push_back( (i+2)%(sectors*2) );

        indices.push_back( i+1 );
        indices.push_back( sectors*2+1 );
        indices.push_back( (i+3)%(2*sectors) );
    }

}

Cylinder::~Cylinder() {
    delete circle;
}


void Cylinder::create_point() {
    circle->create_point();
    std::vector<float> tmp = circle->get_points();
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

    points.push_back(tmp[0]);
    points.push_back(tmp[1]+height/2);
    points.push_back(tmp[2]);

    // std::cout << "y- = " << tmp[3*i+1]-height/2  << '\n';
    points.push_back(tmp[0]);
    points.push_back(tmp[1]-height/2);
    points.push_back(tmp[2]);
}

void Cylinder::create_normals() {
    for (size_t i = 0; i < points.size()/3-2; i+=2) {
        glm::vec3 v0(points[3*i    ],   points[3*i    +1],   points[3*i    +2]);
        glm::vec3 v1(points[3*(i+1)],   points[3*(i+1)+1],   points[3*(i+1)+2]);
        glm::vec3 v2(points[3*( (i+2)%(sectors*2) )],   points[3*((i+2)%(sectors*2)) +1],   points[3*((i+2)%(sectors*2)) +2]);
        // glm::vec3 v3(points[3*(i+3)],   points[3*(i+3)+1],   points[3*(i+3)+2]);
        // std::cout << "v0: " << v0.x << ' ' << v0.y << ' ' << v0.z << '\n';
        // std::cout << "v1: " << v1.x << ' ' << v1.y << ' ' << v1.z << '\n';
        // std::cout << "v2: " << v2.x << ' ' << v2.y << ' ' << v2.z << '\n';
        glm::vec3 c1 = v1 - v0;
        glm::vec3 c2 = v0 - v2;

        glm::vec3 res = glm::normalize(glm::cross(c1, c2));

        normals.insert(normals.end(), glm::value_ptr(res), glm::value_ptr(res)+3);
        normals.insert(normals.end(), glm::value_ptr(res), glm::value_ptr(res)+3);
    }
    glm::vec3 t1(0,1,0);
    glm::vec3 t2(0,-1,0);
    normals.insert(normals.end(), glm::value_ptr(t1), glm::value_ptr(t1)+3);
    normals.insert(normals.end(), glm::value_ptr(t2), glm::value_ptr(t2)+3);
}

// void Cylinder::join_data() {
//     auto points_it = points.begin();
//     auto normals_it = normals.begin();
//     for (size_t i = 0; i < points.size()/3; i++) {
//         norm_and_point.insert(norm_and_point.end(), points_it, points_it+3);
//         norm_and_point.insert(norm_and_point.end(), normals_it, normals_it+3);
//         points_it+=3;
//         normals_it+=3;
//     }
// }
