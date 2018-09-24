class UF:
    def __init__(self, n):
        self.id = list(range(n))
        self.rank = [0]*n

    def find(self,p):
        while p!= self.id[p]:
            self.id[p]= self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        x = self.find(p)
        y = self.find(q)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x

        self.id[self.find(y)] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

if __name__ == '__main__':
    uf = UF(10)
    for (p, q) in [(3, 4), (4, 9), (8, 0), (2, 3), (5, 6), (7, 3), (6, 1)]:
        uf.union(p, q)

    for x in range(10):
        print(uf.find(x))

