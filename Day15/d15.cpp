#include "../IntCodeComputer.hpp"
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <cassert>
#include <cstdlib>
#include <queue>

class Point
{
public:
    int x = 0;
    int y = 0;
    Point(int x, int y)
    {
        this->x = x;
        this->y = y;
    }

    Point(std::string s)
    {
        this->x = stoi(s.substr(0, s.find(",")));
        s.erase(0, s.find(",") + 1);
        this->y = stoi(s);
    }

    std::string hashable()
    {
        return std::to_string(x) + ',' + std::to_string(y);
    }
};

int move(IntCodeComputer &program, Point &curPoint, Point &newPoint)
{
    if (curPoint.hashable() == newPoint.hashable())
    {
        return true;
    }
    if (!((abs(curPoint.x - newPoint.x) == 1 && curPoint.y == newPoint.y) || (abs(curPoint.y - newPoint.y) == 1 && curPoint.x == newPoint.x)))
    {
        return false;
    }
    int prevOutputSize = 0;
    while (program.runSingleCommand())
    {
        if (program.getOutputCount() == prevOutputSize)
        {
            continue;
        }
        prevOutputSize = program.getOutputCount();
        if (curPoint.x < newPoint.x)
        {
            program.setInputValue(4);
        }
        else if (curPoint.x > newPoint.x)
        {
            program.setInputValue(3);
        }
        else if (curPoint.y > newPoint.y)
        {
            program.setInputValue(2);
        }
        else if (curPoint.y < newPoint.y)
        {
            program.setInputValue(1);
        }
        while (program.runSingleCommand())
        {
            if (program.getOutputCount() == prevOutputSize)
            {
                continue;
            }
            prevOutputSize = program.getOutputCount();
            return std::stoi(program.getLastOutput());
        }
    }
}

int moveToPoint(IntCodeComputer &program, Point &curPoint, Point &newPoint, std::unordered_map<std::string, std::string> &path)
{
    if (curPoint.hashable() == newPoint.hashable())
    {
        return true;
    }
    while (!((abs(curPoint.x - newPoint.x) == 1 && curPoint.y == newPoint.y) || (abs(curPoint.y - newPoint.y) == 1 && curPoint.x == newPoint.x)))
    {
        //backtrack
        assert(!path.empty());
        Point parent = Point(path[curPoint.hashable()]);
        bool r = move(program, curPoint, parent);
        assert(r);
        curPoint = parent;
    }
    return move(program, curPoint, newPoint);
}

int bfsMaxPath(Point oxygenPoint, std::unordered_set<std::string> &enabledPoints)
{
    std::unordered_map<std::string, int> dist;
    dist[oxygenPoint.hashable()] = 0;
    std::queue<Point> q;
    q.push(oxygenPoint);
    std::unordered_set<std::string> filled;
    while (!q.empty())
    {
        Point cur = q.front();
        q.pop();
        if (filled.find(cur.hashable()) == filled.end())
        {
            filled.insert(cur.hashable());
            Point adjPoint = Point(cur.x + 1, cur.y);
            if (enabledPoints.find(adjPoint.hashable()) != enabledPoints.end())
            {
                dist[adjPoint.hashable()] = dist[cur.hashable()] + 1;
                q.push(adjPoint);
            }
            adjPoint = Point(cur.x - 1, cur.y);
            if (enabledPoints.find(adjPoint.hashable()) != enabledPoints.end())
            {
                dist[adjPoint.hashable()] = dist[cur.hashable()] + 1;
                q.push(adjPoint);
            }
            adjPoint = Point(cur.x, cur.y + 1);
            if (enabledPoints.find(adjPoint.hashable()) != enabledPoints.end())
            {
                dist[adjPoint.hashable()] = dist[cur.hashable()] + 1;
                q.push(adjPoint);
            }
            adjPoint = Point(cur.x, cur.y - 1);
            if (enabledPoints.find(adjPoint.hashable()) != enabledPoints.end())
            {
                dist[adjPoint.hashable()] = dist[cur.hashable()] + 1;
                q.push(adjPoint);
            }
        }
    }
    int maxPath = 0;
    for (auto &entry : dist)
    {
        maxPath = maxPath < entry.second ? entry.second : maxPath;
    }
    return maxPath - 1;
}

int main()
{
    IntCodeComputer program = IntCodeComputer();
    program.readProgram("input.txt");
    std::vector<Point> stack;
    std::unordered_map<std::string, std::string> path;
    std::unordered_set<std::string> explored;
    stack.push_back(Point(0, 0));
    Point prev = Point(0, 0);
    Point oxygenPoint = Point(0, 0);
    std::unordered_set<std::string> enabledPoints;
    while (!stack.empty())
    {
        Point cur = stack.back();
        stack.pop_back();
        if (explored.find(cur.hashable()) == explored.end())
        {
            explored.insert(cur.hashable());
            switch (moveToPoint(program, prev, cur, path))
            {
            case 0:
                break;
            case 2:
            {
                int count = 1;
                std::string curPtr = prev.hashable();
                while (curPtr != Point(0, 0).hashable() && path.find(curPtr) != path.end())
                {
                    count += 1;
                    curPtr = path[curPtr];
                }
                std::cout << count << std::endl;
                oxygenPoint = cur;
            }
            case 1:
            {
                enabledPoints.insert(cur.hashable());
                path[cur.hashable()] = prev.hashable();
                prev = cur;
                Point adj = Point(cur.x + 1, cur.y);
                stack.push_back(adj);
                adj = Point(cur.x, cur.y + 1);
                stack.push_back(adj);
                adj = Point(cur.x - 1, cur.y);
                stack.push_back(adj);
                adj = Point(cur.x, cur.y - 1);
                stack.push_back(adj);
                break;
            }
            }
        }
    }
    std::cout << bfsMaxPath(oxygenPoint, enabledPoints) << std::endl;
}