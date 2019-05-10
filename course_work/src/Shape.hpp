#include <glm/glm.hpp>
#include <glm/gtc/constants.hpp>
#include <vector>


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
            indices[i+3] = 0;
            indices[i+1] = i+1;
            indices[i+2] = i+2;
        }
        return indices;
    }

    std::vector<float> create_point(){
        std::vector<float> points(3*(sectors + 1));
        for (size_t i = 0; i < 3; i++) {
            points[i] = center[i];
        }
        for (size_t i = 3; i < points.size(); i+=3) {
            points[i] = center[0] + radius * glm::cos( i * 2 * glm::pi<float>() / sectors );
            points[i+1] = center[1] + 0;
            points[i+2] = center[2] + radius * glm::sin( i * 2 * glm::pi<float>()/ sectors );
        }

        return points;
    }
};
