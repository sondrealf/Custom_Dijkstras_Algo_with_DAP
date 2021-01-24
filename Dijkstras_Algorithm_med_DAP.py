INF = 9999999999
shortest = 1
longest = -1
class Graph:
    def __init__(self, graf, method):
        self.graf = graf
        self.method = method
        if method == -1:
            for i in range(len(self.graf)):
                for u in range(len(self.graf[0])):
                    if self.graf[i][u]<INF:
                        self.graf[i][u] *= -1

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

        if map:
            print("--------------")
            print("Til Dist Fra")
            for i in self.map:
                print(i)
            print("--------------")

        if self.method == -1:
            print(min(route)*-1)
        elif not map:
            print("--------------")
            print("Til Dist Fra")
            for i in self.map:
                print(i)
            print("--------------")

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

Longest route or shortest rout?
g = Graph(graf,shortest/longest)

Source, Wanna draw map or not?
g.SSSP(src,True/False)
"""
g = Graph(graf,shortest)
g.SSSP(3,False)
