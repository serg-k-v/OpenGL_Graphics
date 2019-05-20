#include "headers/Sphere.hpp"
#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <vector>
#include <iostream>
// #include <typeinfo>

Sphere::Sphere (glm::vec3 center, float radius, int sectors, int stack, bool movable):Shape() {
    this->center = center;
    this->radius = radius;
    this->sectors = sectors;
    this->stack = stack;
    this->movable = movable;
}

void Sphere::create_indices() {
    int k1, k2;
    for(int i = 0; i < stack; ++i){
        k1 = i * (sectors + 1);     // beginning of current stack
        k2 = k1 + sectors + 1;      // beginning of next stack

        for(int j = 0; j < sectors; ++j, ++k1, ++k2)
        {
            // 2 triangles per sector excluding first and last stacks
            // k1 => k2 => k1+1
            if(i != 0)
            {
                indices.push_back(k1);
                indices.push_back(k2);
                indices.push_back(k1 + 1);
            }

            // k1+1 => k2 => k2+1
            if(i != (stack-1))
            {
                indices.push_back(k1 + 1);
                indices.push_back(k2);
                indices.push_back(k2 + 1);
            }
        }
    }
}

void Sphere::create_point() {
    float x, y, z, xy;                              // vertex position
    float sectorStep = 2 * glm::pi<float>() / sectors;
    float stackStep = glm::pi<float>() / stack;
    float sectorAngle, stackAngle;

    for(int i = 0; i <= stack; ++i)
    {
        stackAngle = glm::pi<float>() / 2 - i * stackStep;        // starting from pi/2 to -pi/2
        xy = radius * cosf(stackAngle);             // r * cos(u)
        z = center.z + radius * sinf(stackAngle);              // r * sin(u)

        for(int j = 0; j <= sectors; ++j)
        {
            sectorAngle = j * sectorStep;           // starting from 0 to 2pi

            // vertex position (x, y, z)
            x = center.x +  xy * cosf(sectorAngle);             // r * cos(u) * cos(v)
            y = center.y + xy * sinf(sectorAngle);             // r * cos(u) * sin(v)
            points.push_back(x);
            points.push_back(y);
            points.push_back(z);
        }
    }
}

void Sphere::create_normals() {
    float x, y, z, xy;                              // vertex position
    float nx, ny, nz, lengthInv = 1.0f / radius;    // vertex normal
    // float s, t;                                     // vertex texCoord

    float sectorStep = 2 * glm::pi<float>() / sectors;
    float stackStep = glm::pi<float>() / stack;
    float sectorAngle, stackAngle;

    for(int i = 0; i <= stack; ++i)
    {
        stackAngle = glm::pi<float>() / 2 - i * stackStep;        // starting from pi/2 to -pi/2
        xy = radius * cosf(stackAngle);             // r * cos(u)
        z = radius * sinf(stackAngle);              // r * sin(u)

        // add (sectors+1) vertices per stack
        // the first and last vertices have same position and normal, but different tex coords
        for(int j = 0; j <= sectors; ++j)
        {
            sectorAngle = j * sectorStep;           // starting from 0 to 2pi

            // vertex position (x, y, z)
            x = xy * cosf(sectorAngle);             // r * cos(u) * cos(v)
            y = xy * sinf(sectorAngle);             // r * cos(u) * sin(v)

            // normalized vertex normal (nx, ny, nz)
            nx = x * lengthInv;
            ny = y * lengthInv;
            nz = z * lengthInv;
            normals.push_back(nx);
            normals.push_back(ny);
            normals.push_back(nz);
        }
    }

}

void Sphere::join_data() {
    auto points_it = points.begin();
    auto normals_it = normals.begin();
    for (size_t i = 0; i < points.size()/3; i++) {
        norm_and_point.insert(norm_and_point.end(), points_it, points_it+3);
        norm_and_point.insert(norm_and_point.end(), normals_it, normals_it+3);
        points_it+=3;
        normals_it+=3;
    }
}
