#ifndef HADER_HPP
#define HADER_HPP

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/rotate_vector.hpp>
#include <vector>
#include <iostream>
#include <functional>

class Shape {
private:

public:
    Shape (){}
    virtual ~Shape (){}
    virtual void create_point() = 0;
    virtual void create_indices() = 0;
    virtual void create_normals() = 0;

    std::vector<float> rotate(const char axis, const float angle, std::vector<float> v) {
        std::vector<float> res;
        for (size_t i = 0; i < v.size()/3; i++) {
            switch (axis) {
                case 'x':{
                    auto tmp = glm::rotateX(glm::vec3(v[3*i], v[3*i+1], v[3*i+2]), angle);
                    res.insert(res.end(), glm::value_ptr(tmp), glm::value_ptr(tmp)+3);}
                    break;
                case 'y':{
                    auto tmp = glm::rotateY(glm::vec3(v[3*i], v[3*i+1], v[3*i+2]), angle);
                    res.insert(res.end(), glm::value_ptr(tmp), glm::value_ptr(tmp)+3);}
                    break;
                case 'z':{
                    auto tmp = glm::rotateZ(glm::vec3(v[3*i], v[3*i+1], v[3*i+2]), angle);
                    res.insert(res.end(), glm::value_ptr(tmp), glm::value_ptr(tmp)+3);}
                    break;
                default :{
                    std::cout << "Incorrect input data!, must be x, y, or z!" << '\n';}
                    break;
            }
        }
        return res;
    }
};

#endif
