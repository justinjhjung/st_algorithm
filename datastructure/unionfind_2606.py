from sys import stdin

def input():
    return stdin.readline().strip()

N = int(input())
M = int(input())
A = []
B = []
for i in range(M):
    a, b = (int(x) for x in input().split())
    A.append(a); B.append(b)

class UnionFind:
    def __init__(self, N, M, A, B):
        self.N = N
        self.M = M
        self.A = A
        self.B = B
        self.parent = [i for i in range(self.N+1)]

    def main(self):
        for i in range(M):
            self.union(self.A[i], self.B[i])

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def replace(self, a, b):
        self.parent = [b if i == a else i for i in self.parent]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a > root_b:
            self.parent[root_a] = root_b
            self.replace(root_a, root_b)
        elif root_a < root_b:
            self.parent[root_b] = root_a
            self.replace(root_b, root_a)

    def __len__(self):
        self.main()
        return self.parent.count(1)

unionfind = UnionFind(N, M, A, B)
print(len(unionfind)-1)
