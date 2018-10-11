from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*len(self.graph) # use hashmaps if strings
        queue = []
        queue.append(s)
        visited[s] = True
        output =[]
        while queue:
            s = queue.pop(0)
            output.append(s)
            print(s, end=" -> ")
            for vertex in self.graph[s]:
                if not visited[vertex]:
                    queue.append(vertex)
                    visited[vertex] = True
        return output

    def DFSUtil(self,s, visited, output):
        visited[s] = True
        print(s, end=" -> ")
        output.append(s)
        for vertex in self.graph[s]:
            if not visited[vertex]:
                self.DFSUtil(vertex,visited, output)
        return output


    def DFS(self):
        visited = defaultdict(bool)# use hashmaps if strings
        out = []
        for i in list(self.graph):
            if visited[i] == False:
                out.append(self.DFSUtil(i, visited,[]))
        return out

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited = defaultdict(bool)
        stack = []
        for i in list(self.graph):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    #g.addEdge(2, 3)
    g.addEdge(3, 4)
    #g.addEdge(4, 3)
    out = g.BFS(2)
    print(out, end="\n")
    out = g.DFS()
    print(out, end="\n")
    G = Graph()
    G.addEdge(5, 2)
    G.addEdge(5, 0)
    G.addEdge(4, 0)
    G.addEdge(4, 1)
    G.addEdge(2, 3)
    G.addEdge(3, 1)
    out = G.topologicalSort()
    print(out, end="\n")
