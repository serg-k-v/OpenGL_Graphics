#include "headers/Torus.hpp"
#include "headers/Circle.hpp"

#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>


Torus::Torus (float sircl_radius, int sirc_sectors,
                float torus_radius, float tor_sectors,
                glm::vec3 center, glm::vec3 color,
                bool half, bool movable):Shape(center, color) {
    // this->center = center;
    this->sircl_radius = sircl_radius;
    this->sirc_sectors = sirc_sectors;
    this->torus_radius = torus_radius;
    this->tor_sectors = tor_sectors;
    this->half = half;
    this->movable = movable;

    create_point();
    create_indices();
}

void Torus::create_indices() {
    int point_c = tor_sectors*sirc_sectors;

    for (size_t i = 0; i < point_c-1-sirc_sectors*int(half); i++) {
        if ((i+1)%sirc_sectors==0)
            i++;
        indices.push_back(i);
        indices.push_back(i+1);
        indices.push_back((i+sirc_sectors+1)%point_c);

        indices.push_back(i);
        indices.push_back((i+sirc_sectors)%point_c);
        indices.push_back((i+sirc_sectors +1)%point_c);
    }

    for (size_t i = 0; i < point_c-sirc_sectors; i+=sirc_sectors) {
        indices.push_back(i + sirc_sectors -1);
        indices.push_back(i);
        indices.push_back((i+sirc_sectors)%point_c);

        indices.push_back(i + sirc_sectors -1);
        indices.push_back((i+2*sirc_sectors -1)%point_c);
        indices.push_back((i+sirc_sectors)%point_c) ;
    }
}

void Torus::create_point() {
    for (size_t i = 0; i < (size_t)tor_sectors; i++) {
        for (size_t j = 0; j < (size_t)sirc_sectors; j++) {

            float x = (torus_radius + sircl_radius* glm::cos( j * 2 * glm::pi<float>() / sirc_sectors))
            * glm::cos( i * ( half ? 1 : 2) * glm::pi<float>() / tor_sectors);
            float y =  (torus_radius + sircl_radius * glm::cos( j * 2 * glm::pi<float>() / sirc_sectors))
            * glm::sin( i * ( half ? 1 : 2) * glm::pi<float>() / tor_sectors);
            float z = sircl_radius * glm::sin( j * 2 * glm::pi<float>() / sirc_sectors);

            points.push_back(x);
            points.push_back(y);
            points.push_back(z);
        }
    }
}

void Torus::create_normals() {
    for (size_t i = 0; i < points.size()/3; i++) {
        glm::vec3 v(points[3*i],   points[3*i+1],   points[3*i+2]);
        glm::vec3 res = glm::normalize(v);
        for (size_t i = 0; i < 3; i++) {
            normals.push_back(res[i]);
        }
    }
}

// void Torus::join_data() {
//     auto points_it = points.begin();
//     auto normals_it = normals.begin();
//     for (size_t i = 0; i < points.size()/3; i++) {
//         norm_and_point.insert(norm_and_point.end(), points_it, points_it+3);
//         norm_and_point.insert(norm_and_point.end(), normals_it, normals_it+3);
//         points_it+=3;
//         normals_it+=3;
//     }
// }
