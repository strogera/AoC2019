#include <iostream>
#include <string>
#include "../IntCodeComputer.hpp"

int main()
{
    IntCodeComputer program = IntCodeComputer();
    program.readProgram("input.txt");
    program.run();
    std::cout << "Day 5" << std::endl;
    std::cout << program.getLastOutput() << std::endl;

    program.reset();
    program.setInputValue(5);
    program.run();
    std::cout << program.getLastOutput() << std::endl;
}
