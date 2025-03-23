#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

void listFiles(const std::string& path) {
    try {
        for (const auto& entry : fs::directory_iterator(path)) {
            std::cout << entry.path().filename() << std::endl;
        }
    } catch (const std::filesystem::filesystem_error& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    std::string directory = "."; // Change this to the directory you want to list
    listFiles(directory);
    return 0;
}
