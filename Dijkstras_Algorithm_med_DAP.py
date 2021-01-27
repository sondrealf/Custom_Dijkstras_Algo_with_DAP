INF = 9999999999
class Graph:
    def __init__(self, graf, method):
        self.method = method

        if isinstance(graf,list):
            self.graf = graf
            if method:
                for i in range(len(self.graf)):
                    for u in range(len(self.graf[0])):
                        if self.graf[i][u]<INF:
                            self.graf[i][u] *= -1
        elif isinstance(graf, int):
            self.graf = []*graf
            for i in range(graf):
                self.graf.append([INF]*graf)

    def SSSP(self, src, map):
        self.map = []*3
        for i in range(len(self.graf)):
            self.map.append([i,INF,""])
        self.visited = []
        self.unvisited = []
        for i in range(len(self.graf)):
            self.unvisited.append(i)

        self.map[src][1] = 0
        self.check(src)
        while not self.unvisited==[]:
            route = []
            for u in range(len(self.graf)):
                route.append(self.map[u][1])
            run = True
            while run:
                try:
                    if not self.visited.index(route.index(min(route))) == []:
                        route[route.index(min(route))] = INF
                except ValueError:
                    run = False
                    self.check(route.index(min(route)))
        route = []
        for u in range(len(self.graf)):
            route.append(self.map[u][1])

        if map or not self.method:
            print("--------------")
            print("Til Dist Fra")
            for i in self.map:
                print(i)
            print("--------------")

        if self.method:
            print(min(route)*-1)

    def check(self, arg):
        teller = []
        for i in range(len(self.graf[0])):
            if self.graf[arg][i]<INF:
                teller.append(i)

        for i in teller:
            if self.graf[arg][i]+self.map[arg][1]<self.map[i][1]:
                try:
                    if not self.visited.index(i)==[]:
                        self.unvisited.append(i)
                        self.visited.pop(self.visited.index(i))
                except ValueError:
                    pass
                self.map[i][2] = arg
                self.map[i][1] = self.graf[arg][i]+self.map[arg][1]
        self.visited.append(arg)
        self.unvisited.pop(self.unvisited.index(arg))

    def addEdge(self, start, end, dist, singel):
        self.graf[start][end] = dist
        if not singel:
            self.graf[end][start] = dist

n = 5
m = 6
liste = ["1 5 26","3 5 2","1 3 20","4 1 10","4 3 23","3 2 13"]

graf = []*n
for i in range(n):
    graf.append([INF]*n)

for i in range(m):
    fra, til, dist = liste[i].split()
    fra = int(fra)-1
    til = int(til)-1
    dist = int(dist)
    graf[fra][til]=dist

"""
Graph becomes
[INF, INF, 20, INF, 26]
[INF, INF, INF, INF, INF]
[INF, 13, INF, INF, 2]
[10, INF, 23, INF, INF]
[INF, INF, INF, INF, INF]

graph or n?, Longest route=True or shortest route=False?
g = Graph(graf/n,True/False)

from index, to index, distance, singel direction=True and both directions=False
g.addEdge(from, to, distance, True/False)

Source, Wanna draw map or not?
g.SSSP(src,True/False)
"""

g = Graph(graf,False)
g.SSSP(3,True)


p = Graph(3,True)
for i in p.graf:
    print(i)
 
print("---------------")

p.addEdge(0, 1, 10, False)
for i in p.graf:
    print(i)
