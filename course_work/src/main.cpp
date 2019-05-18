#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <iostream>

#include "headers/Circle.hpp"
#include "headers/Cylinder.hpp"
#include "headers/Sphere.hpp"
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

    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);

    Shader shader("./src/shaders/Basic.glsl");
    shader.Bind();
    // set up vertex data (and buffer(s)) and configure vertex attributes
    // ------------------------------------------------------------------
    Cylinder* cylinder = new Cylinder(glm::vec3(-1,0,0), 0.4, 0.6, 4); //c, r, h, s
    cylinder->create_point();
    cylinder->create_indices();
    cylinder->create_normals();
    cylinder->join_data();

    Sphere* sphere = new Sphere(glm::vec3(1,0,0), 0.4, 36, 18);
    sphere->create_point();
    sphere->create_indices();
    sphere->create_normals();
    sphere->join_data();

    std::vector<float> try_tt;
    try_tt.insert(try_tt.end(), cylinder->get_n_p().begin(), cylinder->get_n_p().end());
    try_tt.insert(try_tt.end(), sphere->get_n_p().begin(), sphere->get_n_p().end());
    std::vector<int> ind_tt;
    ind_tt.insert(ind_tt.end(), cylinder->get_indices().begin(), cylinder->get_indices().end());
    ind_tt.insert(ind_tt.end(), sphere->get_indices().begin(), sphere->get_indices().end());

    // std::vector<float> fuck{ 0, 0, 0,     0, 0, 0,
    //                          0, 0.2, 0,   -0.2, 0, 0,
    //                          0.2, 0, 0,    0,   0, -0.2,
    //                          0.2, 0, 0.2, -0.2, 0, 0.2};
    // std::vector<int> ind{0,1,2, 0,1,3};

    // std::cout << "\ncylinder points" << '\n';
    // int i = 0;
    // for (const auto &el : cylinder->get_points()) {
    //     std::cout << el << " "; i++;
    //     if ( i%3 == 0){
    //         std::cout << '\n';
    //     }
    // }

    // std::cout << "\ncylinder normals" << '\n';
    // int k = 0;
    // for (const auto &el : cylinder->get_normals()) {
    //     std::cout << el << " "; k++;
    //     if ( k%3 == 0){
    //         std::cout << '\n';
    //     }
    // }
    //
    // std::cout << "\ncylinder join" << '\n';
    // int r = 0;
    // for (const auto &el : cylinder->get_n_p()) {
    //     std::cout << el << " "; r++;
    //     if ( r%6 == 0){
    //         std::cout << '\n';
    //     }
    // }

    unsigned int  VAO;
    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);
    // VertexBuffer vb(cylinder->get_n_p().data(), cylinder->get_n_p().size()*sizeof(float));
    // IndexBuffer ib(cylinder->get_indices().data(), cylinder->get_indices().size());
    VertexBuffer vb(try_tt.data(), try_tt.size()*sizeof(float));
    IndexBuffer ib(ind_tt.data(), ind_tt.size());


    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(float), (void*)(sizeof(float)*3));
    glEnableVertexAttribArray(1);

    // glBindBuffer(GL_ARRAY_BUFFER, 0);
    // glBindVertexArray(0);

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

        shader.SetMat4("projection", projection);
        shader.SetMat4("view", view);
        // shader.SetVec3("viewPos", camera.Position);
        shader.Bind();

        glBindVertexArray(VAO);
        glDrawElements(GL_TRIANGLES, ind_tt.size(), GL_UNSIGNED_INT, 0);

        // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
        // -------------------------------------------------------------------------------
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteVertexArrays(1, &VAO);
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
