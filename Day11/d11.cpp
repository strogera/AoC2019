#include "../IntCodeComputer.hpp"
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <unordered_map>

class Robot
{
private:
    enum Direction
    {
        NORTH,
        EAST,
        SOUTH,
        WEST
    };

    std::map<Direction, Direction> turnRight = {{NORTH, EAST}, {EAST, SOUTH}, {SOUTH, WEST}, {WEST, NORTH}};
    std::map<Direction, Direction> turnLeft = {{EAST, NORTH}, {SOUTH, EAST}, {WEST, SOUTH}, {NORTH, WEST}};
    Direction direction;

public:
    Robot(bool part2 = false)
    {
        direction = part2 ? WEST : EAST;
    }
    int posx = 0;
    int posy = 0;
    void move(int newDirection)
    {
        direction = newDirection == 0 ? turnLeft[direction] : turnRight[direction];

        switch (direction)
        {
        case NORTH:
            posy += 1;
            break;
        case SOUTH:
            posy -= 1;
            break;
        case EAST:
            posx += 1;
            break;
        case WEST:
            posx -= 1;
            break;
        }
    }

    std::string getPosition()
    {
        return std::to_string(posx) + std::to_string(posy);
    }
};

void runRobot(Robot &robot, IntCodeComputer &program, std::unordered_map<std::string, int> &grid, int grid2[][45], bool part2 = false)
{
    int lastOutputSize = 0;
    int color = 0;
    while (program.runSingleCommand())
    {
        int curOutputSize = program.getOutputCount();
        if (curOutputSize == lastOutputSize + 1)
        {
            int curOutput = std::stoi(program.getLastOutput());
            color = curOutput;
            continue;
        }
        if (curOutputSize == lastOutputSize + 2)
        {
            int curOutput = std::stoi(program.getLastOutput());
            grid[robot.getPosition()] = color;
            if (part2)
            {
                grid2[1 + robot.posx][2 + robot.posy] = color;
            }
            robot.move(curOutput);
            program.setInputValue(grid[robot.getPosition()]);
        }
        lastOutputSize = curOutputSize;
    }
}

int main()
{
    std::unordered_map<std::string, int> grid;
    IntCodeComputer program = IntCodeComputer(0);
    program.readProgram("input.txt");

    Robot robot = Robot();
    int grid2[8][45];
    for (int x = 0; x < 8; x++)
    {
        for (int y = 0; y < 45; y++)
        {
            grid2[x][y] = 0;
        }
    }

    runRobot(robot, program, grid, grid2, false);

    std::cout << grid.size() << std::endl;

    program.reset();
    program.setInputValue(1);
    Robot robot2 = Robot(true);
    grid.empty();
    runRobot(robot2, program, grid, grid2, true);
    for (auto &x : grid2)
    {
        for (auto &y : x)
        {
            char p = y == 1 ? '#' : ' ';
            std::cout << p;
        }
        std::cout << std::endl;
    }
}