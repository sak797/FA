from collections import defaultdict
import heapq
import unionfind

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

class UGraph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, w):
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def PrimMST(self): # doesn't have the complexity ElogV. It is more. I need to use specialized heap where I know the positions of my vertices in heap in O(1)
        heap = []
        for vertex in list(self.graph):
            heapq.heappush(heap, [9999, vertex])
        first_vertex = heap[0]
        first_vertex[0] = 0
        heap[0] = first_vertex
        heapq.heapify(heap)
        parent= defaultdict(int)
        parent[first_vertex[1]] = -1
        while len(heap):
            node = heapq.heappop(heap)
            # find the dnode in heap and update the distance
            for dnode in self.graph[node[1]]:
                dest, dist = dnode
                for i in range(len(heap)):
                    if heap[i][1] == dest:
                        if heap[i][0] > dist:
                            heap[i][0] = dist
                            parent[dest] = node[1]
                            heapq.heapify(heap)
                            break
        for i in list(parent):
            print(i, " --> ", parent[i], end="\n")

    def KruskalMST(self):
        result = []
        count1 = 0
        count2 = 0
        # convert self.graph to [u,v,w]
        unique_edges = set()
        for svertex in list(self.graph):
            for dvertex in self.graph[svertex]:
                temp1 = (svertex, dvertex[0], dvertex[1])
                temp2 = (dvertex[0], svertex, dvertex[1])
                if temp1 in unique_edges or temp2 in unique_edges:
                    pass
                else:
                    unique_edges.add(temp1)

        unique_edges = sorted(unique_edges, key = lambda x: x[2])
        print(unique_edges)
        uf = unionfind.UF(len(self.graph))
        while count1 < len(self.graph) and count2 < len(unique_edges):
            temp = unique_edges[count2]
            x = uf.find(temp[0])
            y = uf.find(temp[1])
            count2 += 1
            if x != y:
                uf.union(x,y)
                result.append(temp)
                count1 += 1
        for item in result:
            print(item[0], " --> ", item[1])





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

    u = UGraph()
    u.addEdge(0, 1, 4)
    u.addEdge(0, 7, 8)
    u.addEdge(1, 2, 8)
    u.addEdge(1, 7, 11)
    u.addEdge(2, 3, 7)
    u.addEdge(2, 8, 2)
    u.addEdge(2, 5, 4)
    u.addEdge(3, 4, 9)
    u.addEdge(3, 5, 14)
    u.addEdge(4, 5, 10)
    u.addEdge(5, 6, 2)
    u.addEdge(6, 7, 1)
    u.addEdge(6, 8, 6)
    u.addEdge(7, 8, 7)
    u.PrimMST()
    print("Kruskal: ")
    u.KruskalMST()
