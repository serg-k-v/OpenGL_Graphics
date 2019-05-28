#include "headers/Torus.hpp"
#include "headers/Circle.hpp"

#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>


Torus::Torus (glm::vec3 center, float sircl_radius, int sirc_sectors, float torus_radius, float tor_sectors, bool movable):Shape() {
    this->center = center;
    this->sircl_radius = sircl_radius;
    this->sirc_sectors = sirc_sectors;
    this->torus_radius = torus_radius;
    this->tor_sectors = tor_sectors;
    this->movable = movable;
    try{
        this->circle = new Circle(center, sircl_radius, sirc_sectors);
    }catch(const std::bad_alloc& e){
        std::cout << "Allocation failed: " << e.what() << '\n';
        exit (EXIT_FAILURE);
    }

    create_point();
    create_indices();
}

void Torus::create_indices() {
    int point_c = tor_sectors*sirc_sectors;
    for (size_t i = 0; i < point_c-1; i++) {
        if ((i+1)%sirc_sectors==0)
            i++;
        indices.push_back(i);
        indices.push_back(i+1);
        indices.push_back((i+sirc_sectors+1)%point_c);

        indices.push_back(i);
        indices.push_back((i+sirc_sectors)%point_c);
        indices.push_back((i+sirc_sectors +1)%point_c);
    }

    for (size_t i = 0; i < point_c; i+=sirc_sectors) {
        indices.push_back(i + sirc_sectors -1);
        indices.push_back(i);
        indices.push_back((i+sirc_sectors)%point_c);

        indices.push_back(i + sirc_sectors -1);
        indices.push_back((i+2*sirc_sectors -1)%point_c);
        indices.push_back((i+sirc_sectors)%point_c) ;
    }
}

void Torus::create_point() {
    circle->create_point();
    std::vector<float> crcl = circle->rotate('x', glm::pi<float>()/2, circle->get_points());
    crcl.erase(crcl.begin(), crcl.begin()+3); //delete center cordinate
    std::cout << "points of circle" << '\n';
    int l = 1;
    for (auto &el : crcl) {
        std::cout << el << ' ';
        if (l%3 == 0)
            std::cout << '\n';
        l++;
    }

    for (size_t i = 0; i < (size_t)tor_sectors; i++) {
        for (size_t j = 0; j < (size_t)sirc_sectors; j++) {

            float x = (torus_radius + sircl_radius* glm::cos( j * 2 * glm::pi<float>() / sirc_sectors)) * glm::cos( i * 2 * glm::pi<float>() / tor_sectors);
            float y =  sircl_radius * glm::sin( j * 2 * glm::pi<float>() / sirc_sectors);
            float z = (torus_radius + sircl_radius * glm::cos( j * 2 * glm::pi<float>() / sirc_sectors)) * glm::sin( i * 2 * glm::pi<float>() / tor_sectors);

            // std::cout << "i : " <<  i << ' ';
            // std::cout << "j : "  << j << ' ';
            // std::cout << "cos : " <<  glm::cos( i * 2 * glm::pi<float>() / tor_sectors) << ' ';
            // std::cout << "sin : " <<  glm::sin( i * 2 * glm::pi<float>() / tor_sectors) << '\n';
            points.push_back(x);
            points.push_back(y);
            points.push_back(z);
        }
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

Torus::~Torus() {
    delete circle;
}
