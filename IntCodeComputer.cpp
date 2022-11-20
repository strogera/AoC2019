
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <numeric>
#include <unordered_map>

#include "IntCodeComputer.hpp"

#define POSITIONAL '0'
#define IMMIDIATE '1'
#define RELATIVE '2'

class OpCode
{
public:
    int code;
    long long argPos1 = 0;
    long long argPos2 = 0;
    long long argPos3 = 0;

    OpCode(long long codePos, std::unordered_map<long long, long long> &memory, long long relativeBase)
    {
        std::string codeStr = std::to_string(memory[codePos]);
        code = codeStr.length() <= 2 ? stoi(codeStr) : stoi(codeStr.substr(codeStr.length() - 2));

        auto getArgPos = [&memory, relativeBase](char c, long long argPos)
        {
            switch (c)
            {
            case POSITIONAL:
                return memory[argPos];
            case IMMIDIATE:
                return argPos;
            case RELATIVE:
                return relativeBase + memory[argPos];
            default:
                std::cerr << "wrong code" << std::endl;
                exit(0);
            }
        };

        argPos1 = getArgPos(codeStr.length() >= 3 ? codeStr[codeStr.length() - 3] : POSITIONAL, codePos + 1);
        argPos2 = getArgPos(codeStr.length() >= 4 ? codeStr[codeStr.length() - 4] : POSITIONAL, codePos + 2);
        argPos3 = getArgPos(codeStr.length() >= 5 ? codeStr[codeStr.length() - 5] : POSITIONAL, codePos + 3);
    }
};

std::vector<std::string> IntCodeComputer::split(std::string s, std::string delim)
{
    std::vector<std::string> res;
    size_t pos = 0, end = 0;
    std::string token;
    while ((pos = s.find(delim, end)) != std::string::npos)
    {
        res.push_back(s.substr(end, pos - end));
        end = pos + 1;
    }
    res.push_back(s.substr(end));
    return res;
}

void IntCodeComputer::add(long long a, long long b, long long res)
{
    memory[res] = memory[a] + memory[b];
}

void IntCodeComputer::mult(long long a, long long b, long long res)
{
    memory[res] = memory[a] * memory[b];
}

void IntCodeComputer::input(long long a)
{
    memory[a] = inputValue;
}

void IntCodeComputer::output(long long a)
{
    outputHistory.push_back(memory[a]);
}

long long IntCodeComputer::jit(long long a, long long b)
{
    return (memory[a] != 0) ? memory[b] : ip + 3;
}

long long IntCodeComputer::jif(long long a, long long b)
{
    return (memory[a] == 0) ? memory[b] : ip + 3;
}

void IntCodeComputer::lt(long long a, long long b, long long res)
{
    memory[res] = (memory[a] < memory[b]) ? 1 : 0;
}

void IntCodeComputer::eq(long long a, long long b, long long res)
{
    memory[res] = (memory[a] == memory[b]) ? 1 : 0;
}

void IntCodeComputer::adjustRelativeBase(long long a)
{
    relativeBase += memory[a];
}

IntCodeComputer::IntCodeComputer(int inputVal)
{
    inputValue = inputVal;
}
void IntCodeComputer::readProgram(std::string inputFilePath)
{
    std::ifstream inputFile(inputFilePath);
    if (inputFile.is_open())
    {
        std::string line;
        while (std::getline(inputFile, line))
        {
            std::vector<std::string> splittedLine(split(line, ","));
            int i = 0;
            for (auto cur : splittedLine)
            {
                memory[i] = std::stoll(cur);
                originalOpCodes[i] = std::stoll(cur);
                i++;
            }
        }
        inputFile.close();
    }
    else
    {
        std::cerr << "error with input file" << std::endl;
    }
}

void IntCodeComputer::run()
{
    while (runSingleCommand())
    {
    }
}

bool IntCodeComputer::runSingleCommand()
{
    if (memory[ip] != 99)
    {
        ip = runCodeAt(ip);
    }
    return memory[ip] != 99;
}

void IntCodeComputer::reset()
{
    memory = originalOpCodes;
    ip = 0;
    outputHistory = {};
    relativeBase = 0;
}

long long IntCodeComputer::runCodeAt(long long i)
{
    OpCode code(i, memory, relativeBase);
    switch (code.code)
    {
    case 1:
        add(code.argPos1, code.argPos2, code.argPos3);
        return ip + 4;
    case 2:
        mult(code.argPos1, code.argPos2, code.argPos3);
        return ip + 4;
    case 3:
        input(code.argPos1);
        return ip + 2;
    case 4:
        output(code.argPos1);
        return ip + 2;
    case 5:
        return jit(code.argPos1, code.argPos2);
    case 6:
        return jif(code.argPos1, code.argPos2);
    case 7:
        lt(code.argPos1, code.argPos2, code.argPos3);
        return ip + 4;
    case 8:
        eq(code.argPos1, code.argPos2, code.argPos3);
        return ip + 4;
    case 9:
        adjustRelativeBase(code.argPos1);
        return ip + 2;
    default:
        std::cout << "ended with code " << code.code << std::endl;
        exit(0);
    }
}

long long IntCodeComputer::getOpCodeAt(long long i)
{
    return memory[i];
}

void IntCodeComputer::changeOpCodeAt(long long i, long long newValue)
{
    memory[i] = newValue;
}

std::string IntCodeComputer::getLastOutput()
{
    return outputHistory.empty() ? "" : std::to_string(outputHistory.back());
}

int IntCodeComputer::getOutputCount()
{
    return outputHistory.size();
}

void IntCodeComputer::setInputValue(long long newValue)
{
    inputValue = newValue;
}

void IntCodeComputer::setMemoryAt(long long i, long long value)
{
    memory[i] = value;
}
