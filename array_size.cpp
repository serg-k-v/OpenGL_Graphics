#include <iostream>




int main(int argc, char const *argv[]) {
    const int n = 3;
    float** arr = new float*[n];
    for (size_t i = 0; i < n; i++) {
        arr[i] = new float[n];
    }
    std::cout << "[";
    for (size_t i = 0; i < n; i++) {
        std::cout << '\n';
        for (size_t j = 0; j < n; j++) {
            std::cout << arr[i][j] << ' ';
        }
    }
    std::cout << "]" << '\n';
    std::cout << "size : " << sizeof(arr[0][0])*9 << '\n';
    return 0;
}
