#include "../IntCodeComputer.hpp"
#include <unordered_map>
#include <string>
#include <iostream>

int main()
{
    IntCodeComputer program = IntCodeComputer(0);
    program.readProgram("input.txt");
    int count = 0;
    int lastOutputSize = 0;
    int args[3] = {0, 0, 0};
    int c = 0;
    while (program.runSingleCommand())
    {
        int curOutputSize = program.getOutputCount();
        if (curOutputSize != lastOutputSize)
        {
            args[c] = std::stoi(program.getLastOutput());
            c += 1;
            if (c == 3)
            {
                if (args[2] == 2)
                {
                    count += 1;
                }
                c = 0;
            }
        }
        lastOutputSize = curOutputSize;
    }
    std::cout << count << std::endl;

    program.reset();
    program.setMemoryAt(0, 2);
    lastOutputSize = 0;
    c = 0;
    int paddleHorPos = 0;
    int score = 0;
    while (program.runSingleCommand())
    {
        int curOutputSize = program.getOutputCount();
        if (curOutputSize != lastOutputSize)
        {
            args[c] = std::stoi(program.getLastOutput());
            c += 1;
            if (c == 3)
            {
                if (args[0] == -1)
                {
                    score = args[2];
                }
                if (args[2] == 3)
                {
                    paddleHorPos = args[0];
                }
                if (args[2] == 4)
                {
                    if (paddleHorPos == args[0])
                    {
                        program.setInputValue(0);
                    }
                    else if (paddleHorPos < args[0])
                    {
                        program.setInputValue(1);
                    }
                    else if (paddleHorPos > args[0])
                    {
                        program.setInputValue(-1);
                    }
                }
                c = 0;
            }
        }
        lastOutputSize = curOutputSize;
    }
    std::cout << score << std::endl;
}