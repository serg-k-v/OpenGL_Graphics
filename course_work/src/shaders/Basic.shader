#shader vertex
#version 330 core
layout (location = 0) in vec3 aPos;
// layout (location = 1) in vec3 aNorm;
out vec3 FragPos;
void main(){
    FragPos = aPos;
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}

#shader fragment
#version 330 core
out vec4 FragColor;
in vec3 FragPos;
/* vec3 aNormal = vec3(0.0f, 0.0f, 1.0f); */
float ambientStrength = 0.1f;
vec3 lightColor = vec3(1.0, 1.0, 1.0);
vec3 objectColor = vec3(1.0f, 0.5f, 0.2f);
vec3 lightPos = vec3(1.0f, 1.0f, 1.0f);

vec3 ambient = ambientStrength * lightColor;
vec3 norm = normalize(vec3(0.0, 0.0, 1.0));
vec3 tmp = lightPos - FragPos;
vec3 lightDir = normalize(tmp);

float diff = max(dot(norm, lightDir), 0.0);
vec3 diffuse = diff * lightColor;
vec3 result = (ambient + diffuse) * objectColor;

void main(){
    FragColor = vec4(result, 1.0);
}
