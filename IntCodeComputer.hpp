#ifndef INTCODECOMPUTER_HPP
#define INTCODECOMPUTER_HPP
#include <vector>
#include <unordered_map>
#include <string>

class IntCodeComputer
{
private:
    std::unordered_map<long long, long long> memory;
    std::unordered_map<long long, long long> originalOpCodes;
    std::vector<long long> outputHistory;
    long long ip = 0;
    long long inputValue;
    long long relativeBase = 0;

    std::vector<std::string> split(std::string, std::string);
    void add(long long, long long, long long);
    void mult(long long, long long, long long);
    void input(long long);
    void output(long long);
    long long jit(long long, long long);
    long long jif(long long, long long);
    void lt(long long, long long, long long);
    void eq(long long, long long, long long);
    void adjustRelativeBase(long long);

public:
    IntCodeComputer(int inputValue = 1);
    void readProgram(std::string);
    void run();
    bool runSingleCommand();
    void reset();
    long long runCodeAt(long long);
    long long getOpCodeAt(long long);
    void changeOpCodeAt(long long, long long);
    std::string getLastOutput();
    int getOutputCount();
    void setInputValue(long long);
    void setMemoryAt(long long, long long);
};
#endif