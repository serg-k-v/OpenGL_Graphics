#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <iostream>
#include <array>

#include "headers/Circle.hpp"
#include "headers/Cylinder.hpp"
#include "headers/Sphere.hpp"
#include "headers/Torus.hpp"
#include "headers/Camera.hpp"
#include "headers/Shader.hpp"
#include "headers/VertexBuffer.hpp"
#include "headers/IndexBuffer.hpp"

void framebuffer_size_callback(GLFWwindow* window, int width, int height);
void processInput(GLFWwindow *window);

void mouse_callback(GLFWwindow* window, double xpos, double ypos);
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset);

// settings
const unsigned int SCR_WIDTH = 900;
const unsigned int SCR_HEIGHT = 900;

Camera camera(glm::vec3(0.0f, 0.0f, 3.0f));
float lastX = SCR_WIDTH / 2.0f;
float lastY = SCR_HEIGHT / 2.0f;
bool firstMouse = true;

// timing
float deltaTime = 0.0f;
float lastFrame = 0.0f;

int main()
{
    // glfw: initialize and configure
    // ------------------------------
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    // glfw window creation
    // --------------------
    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);
    glfwSetCursorPosCallback(window, mouse_callback);
    glfwSetScrollCallback(window, scroll_callback);

    // tell GLFW to capture our mouse
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

    // glad: load all OpenGL function pointers
    // ---------------------------------------
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    // Lightining setup

    // glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    // glEnable(GL_LIGHTING);
    // glEnable(GL_LIGHT0);


    // ------------------------------------------------------------------
    Torus*    torus_full_1 = new Torus(glm::vec3(0,0,0), 0.025, 15, 0.9, 36); //c, r, s1, R, s2, half
    torus_full_1->create_normals();
    torus_full_1->join_data();

    Sphere*   sphere_base = new Sphere(glm::vec3(0,0,0), 0.2, 32, 16);
    sphere_base->create_normals();
    sphere_base->join_data();

    // std::cout << "Torus points" << '\n';
    // int k = 1;
    // for (auto &el : torus->get_points()) {
    //     std::cout << el << ' ';
    //     if(k%3 == 0)
    //         std::cout << '\n';
    //     k++;
    // }
    // std::cout << "Torus indices" << '\n';
    // int j = 1;
    // for (auto &el : torus->get_indices()) {
    //     std::cout << el << ' ';
    //     if(j%3 == 0)
    //         std::cout << '\n';
    //     j++;
    // }


    Shader shader("./src/shaders/Basic.glsl");
    shader.Bind();

    std::vector<std::vector<float>> arr_vb = {  torus_full_1->get_n_p(),
                                                sphere_base->get_n_p()};
    std::vector<std::vector<int>>   arr_ib = {  torus_full_1->get_indices(),
                                                sphere_base->get_indices()};

    const size_t n = arr_vb.size();
    std::cout << "size : " << n << '\n';
    unsigned int *VAO = new unsigned int[n];
    unsigned int *VBO = new unsigned int[n];
    unsigned int *IBO = new unsigned int[n];

    for (size_t i = 0; i < n; i++) {
        glGenVertexArrays(n, &VAO[i]);
        glBindVertexArray(VAO[i]);

        glGenBuffers(n, &VBO[i]);
        glBindBuffer(GL_ARRAY_BUFFER, VBO[i]);
        glBufferData(GL_ARRAY_BUFFER, arr_vb[i].size()*sizeof(float), arr_vb[i].data(), GL_STATIC_DRAW);
        // VBO[i] = VertexBuffer(arr_vb[i].data(), arr_vb[i].size()*sizeof(float)); //не работает!!1
        glGenBuffers(n, &IBO[i]);
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, IBO[i]);
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, arr_ib[i].size()*sizeof(int), arr_ib[i].data(), GL_STATIC_DRAW);
        // IBO[i] = IndexBuffer(arr_ib[i].data(), arr_ib[i].size()); //не работает!!1

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
        glEnableVertexAttribArray(0);

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(sizeof(float)*3));
        glEnableVertexAttribArray(1);
    }

    Cylinder*   sphere_test = new Cylinder(glm::vec3(0,0,1), 0.5, 1, 5);
    sphere_test->create_normals();
    sphere_test->join_data();

    Shader test_shader("./src/shaders/Basic.glsl");
    test_shader.Bind();

    unsigned int test_VAO;
    unsigned int test_VBO;
    unsigned int test_IBO;


    glGenVertexArrays(1, &test_VAO);
    glBindVertexArray(test_VAO);
    //
    glGenBuffers(1, &test_VBO);
    glBindBuffer(GL_ARRAY_BUFFER, test_VBO);
    glBufferData(GL_ARRAY_BUFFER,sphere_test->get_points().size()*sizeof(float), sphere_test->get_points().data(), GL_STATIC_DRAW);
    // VertexBuffer vb(sphere_test->get_points().data(), sphere_test->get_points().size()*sizeof(float));
    glGenBuffers(1, &test_IBO);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, test_IBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sphere_test->get_indices().size()*sizeof(int), sphere_test->get_indices().data(), GL_STATIC_DRAW);
    // IndexBuffer ib(sphere_test->get_indices().data(), sphere_test->get_indices().size());

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(sizeof(float)*3));
    glEnableVertexAttribArray(1);


    // render loop
    // -----------
    while (!glfwWindowShouldClose(window))
    {
        float currentFrame = glfwGetTime();
        deltaTime = currentFrame - lastFrame;
        lastFrame = currentFrame;
        // input
        // -----
        processInput(window);
        // render
        // ------
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glm::mat4 projection = glm::perspective(glm::radians(camera.Zoom), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
        glm::mat4 view = camera.GetViewMatrix();
        //
        shader.SetMat4("projection", projection);
        shader.SetMat4("view", view);
        // shader.SetVec3("viewPos", camera.Position);

        shader.Bind(); //????????????????????????????
        for (size_t i = 0; i < n; i++) {
            glBindVertexArray(VAO[i]);
            glDrawElements(GL_TRIANGLES, arr_ib[i].size(), GL_UNSIGNED_INT, 0);
        }

        test_shader.SetMat4("projection", projection);
        test_shader.SetMat4("view", view);
        // test_shader.SetVec3("viewPos", camera.Position);

        test_shader.Bind();
        glBindVertexArray(test_VAO);
        glDrawElements(GL_TRIANGLES, sphere_test->get_indices().size(), GL_UNSIGNED_INT, 0);

        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        // -------------------------------------------------------------------------------
        glfwSwapBuffers(window);
        glfwPollEvents();
    }
    // shader.Unbind();
    // for (size_t i = 0; i < n; i++) {
    //     glDeleteVertexArrays(n, &VAO[i]);
    // }

    // glfw: terminate, clearing all previously allocated GLFW resources.
    // ------------------------------------------------------------------
    glfwTerminate();
    return 0;
}

// process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
// ---------------------------------------------------------------------------------------------------------
void processInput(GLFWwindow *window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
    if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
        camera.ProcessKeyboard(FORWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
        camera.ProcessKeyboard(BACKWARD, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
        camera.ProcessKeyboard(LEFT, deltaTime);
    if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
        camera.ProcessKeyboard(RIGHT, deltaTime);
}

// glfw: whenever the window size changed (by OS or user resize) this callback function executes
// ---------------------------------------------------------------------------------------------
void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    // make sure the viewport matches the new window dimensions; note that width and
    // height will be significantly larger than specified on retina displays.
    glViewport(0, 0, width, height);
}


// glfw: whenever the mouse moves, this callback is called
// -------------------------------------------------------
void mouse_callback(GLFWwindow* window, double xpos, double ypos)
{
    if (firstMouse)
    {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }

    float xoffset = xpos - lastX;
    float yoffset = lastY - ypos; // reversed since y-coordinates go from bottom to top

    lastX = xpos;
    lastY = ypos;

    camera.ProcessMouseMovement(xoffset, yoffset);
}

// glfw: whenever the mouse scroll wheel scrolls, this callback is called
// ----------------------------------------------------------------------
void scroll_callback(GLFWwindow* window, double xoffset, double yoffset)
{
    camera.ProcessMouseScroll(yoffset);
}
