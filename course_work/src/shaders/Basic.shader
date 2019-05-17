#shader vertex
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNorm;

out vec3 FragPos;
out vec3 Normal;

uniform mat4 view;
uniform mat4 projection;

void main(){
    FragPos = aPos;
    Normal = aNorm;
    gl_Position = projection * view * vec4(aPos.x, aPos.y, aPos.z, 1.0);
}

#shader fragment
#version 330 core
out vec4 FragColor;

in vec3 FragPos;
in vec3 Normal;

void main(){
    float ambientStrength = 0.1;
    vec3 lightColor = vec3(1.0, 1.0, 1.0);
    vec3 objectColor = vec3(1.0, 0.5, 0.2);
    vec3 lightPos = vec3(1.0, 1.0, 1.0);

    vec3 ambient = ambientStrength * lightColor;
    // vec3 norm = normalize(vec3(0.0, 0.0, 1.0));
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    vec3 result = (ambient + diffuse) * objectColor;

    FragColor = vec4(result, 1.0);
}
