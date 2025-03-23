cmake_minimum_required(VERSION 3.10)
project(HueAndCry)

# Set C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
include_directories(include)

# Add subdirectories (for modular projects)
add_subdirectory(src)