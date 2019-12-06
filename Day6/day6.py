def dfs(graph, v):
   stack=[] 
   discovered=set()
   count=0
   stack.append((v, count))
   countall=0
   while stack:
       (v, count)=stack.pop()
       countall+=count
       if v not in discovered:
           discovered.add(v)
           if v in graph:
               for w in graph[v]:
                   stack.append((w, count+1))
   return countall

def dfs2(graph, source, target):
   stack=[] 
   discovered=set()
   count=0
   stack.append((source, count))
   countList=[]
   while stack:
       (v, count)=stack.pop()
       if v == target:
           countList.append(count)
           continue
       if v not in discovered:
           discovered.add(v)
           if v in graph:
               for w in graph[v]:
                   stack.append((w, count+1))
   return min(countList)

def partOne():
    with open("input.txt", "r") as inputFile:
        graph={}
        for line in inputFile:
            A, B= line.strip().split(')')
            if A in graph:
                graph[A].append(B)
            else:
                graph[A]=[B]
        print(dfs(graph, "COM"))



def partTwo():
    with open("input.txt", "r") as inputFile:
        graph={} 
        for line in inputFile:
            A, B= line.strip().split(')')
            if A in graph:
                graph[A].append(B)
            else:
                graph[A]=[B]
            if B in graph:
                graph[B].append(A)
            else:
                graph[B]=[A]

        pathLen=[]
        for adjY in graph["YOU"]:
            for adjS in graph["SAN"]:
                pathLen.append(dfs2(graph, adjY, adjS))
        print(min(pathLen))


print("Answer for part one: ")
partOne()
print("Answer for part two: ")
partTwo()
