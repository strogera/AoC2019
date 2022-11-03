#include <iostream>
#include <string>
#include "../IntCodeComputer.hpp"

int main()
{
    IntCodeComputer program = IntCodeComputer();
    program.readProgram("input.txt");
    program.run();
    std::cout << "Day 2" << std::endl;
    std::cout << program.getOpCodeAt(0) << std::endl;

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            program.reset();
            program.changeOpCodeAt(1, i);
            program.changeOpCodeAt(2, j);
            program.run();
            if (program.getOpCodeAt(0) == 19690720)
            {
                std::cout << 100 * i + j << std::endl;
                exit(0);
            }
        }
    }
}
