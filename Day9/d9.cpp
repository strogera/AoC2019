#include <iostream>
#include <string>
#include "../IntCodeComputer.hpp"

int main()
{
    IntCodeComputer program = IntCodeComputer(1);
    program.readProgram("input.txt");
    program.run();
    std::cout << "Day 9" << std::endl;
    std::cout << program.getLastOutput() << std::endl;

    program.reset();
    program.setInputValue(2);
    program.run();
    std::cout << program.getLastOutput() << std::endl;
}