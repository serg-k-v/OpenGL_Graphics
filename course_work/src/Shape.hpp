#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>
#include <iostream>
#include <cmath>
// #define M_PI 3.141592653
class Shape {
private:

public:
    Shape (){}
    virtual ~Shape (){}
    virtual std::vector<float> create_point() = 0;
    virtual std::vector<int> create_indices() = 0;
};

class Circle : public Shape {
private:
    glm::vec3 center;
    float radius;
    int sectors;
    bool movable = false;

public:
    Circle (glm::vec3 center, float radius, int sectors, bool movable = false):Shape(){
        this->center = center;
        this->radius = radius;
        this->sectors = sectors;
        this->movable = movable;
    }

    std::vector<int> create_indices(){
        std::vector<int> indices(3*sectors);
        for (size_t i = 0; i < sectors; i++) {
            indices[3*i] = 0;
            indices[3*i+1] = i+1;
            indices[3*i+2] = i+2 <= sectors ? i+2 : 1 ;
        }
        return indices;
    }
    std::vector<float> create_point(){
        std::vector<float> points;
        for (size_t i = 0; i < 3; i++) {
            points.push_back(center[i]);
        }
        std::cout << "/* message */" << '\n';
        for (size_t i = 0; i < sectors; i++) {
            std::cout << i << ' '
                      << cos( float(i * 2 * M_PI / sectors) ) << ' '
                      << sin( float(i * 2 * M_PI / sectors) ) << '\n';
            points.push_back(center[0] + radius * cos( i * 2 * M_PI / sectors ));
            points.push_back(center[1] + radius * sin( i * 2 * M_PI/ sectors ));
            points.push_back(center[2] + 0);
        }

        return points;
    }

    
};
