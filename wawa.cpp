#include <string>
#include <cstdlib>
#include <iostream>

int main(int argc, char* argv[]) {
    //std::string cmd = "\"python wawa.py ";
    std::string cmd = "\"ls";
    for (int i = 1; i < argc; i++) {
        cmd += " ";
        cmd += argv[i];
    }
    cmd += "\"";
    //std::cout << cmd;
    std::system(cmd.c_str());
    return 0;
}
