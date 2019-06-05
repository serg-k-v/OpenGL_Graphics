#ifndef HADER_HPP
#define HADER_HPP

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/rotate_vector.hpp>
#include <vector>
#include <iostream>
#include <functional>

class Shape {
protected:
    glm::vec3 center;
    glm::vec3 color;
    std::vector<int>  indices;
    std::vector<float>  points;
    std::vector<float>  normals;
    std::vector<float>  norm_and_point;
public:
    Shape (glm::vec3 center = glm::vec3(0, 0, 0), glm::vec3 color = glm::vec3(1, 0.5, 0.2)):center(center), color(color){}
    virtual ~Shape (){}
    virtual void create_point() = 0;
    virtual void create_indices() = 0;
    virtual void create_normals() = 0;

    const std::vector<int> &get_indices() const {return indices;}
    const std::vector<float> &get_points() const {return points;}
    const std::vector<float> &get_normals() const {return normals;}

    void join_data() {
        auto points_it = points.begin();
        auto normals_it = normals.begin();
        for (size_t i = 0; i < points.size()/3; i++) {
            norm_and_point.insert(norm_and_point.end(), points_it, points_it+3);
            norm_and_point.insert(norm_and_point.end(), normals_it, normals_it+3);
            norm_and_point.insert(norm_and_point.end(), glm::value_ptr(color), glm::value_ptr(color)+3);
            points_it+=3;
            normals_it+=3;
        }
    }

    virtual void rotate(const char axis, const float angle) {
        for (auto it = points.begin(); it <= points.end()-3; it+=3) {
            glm::vec3 tmp;
            switch (axis) {
                case 'x':{
                    tmp = glm::rotateX(glm::vec3(*it - center.x, *(it+1) - center.y, *(it+2)) - center.z, angle);}
                    break;
                case 'y':{
                    tmp = glm::rotateY(glm::vec3(*it - center.x, *(it+1) - center.y, *(it+2)) - center.z, angle);}
                    break;
                case 'z':{
                    tmp = glm::rotateZ(glm::vec3(*it - center.x, *(it+1) - center.y, *(it+2)) - center.z, angle);}
                    break;
                default :{
                    std::cout << "Incorrect input data!, must be x, y, or z!" << '\n';}
                    break;
            }
            *it = tmp.x + center.x;
            *(it+1) = tmp.y + center.y;
            *(it+2) = tmp.z + center.z;
        }
    }
};

#endif
