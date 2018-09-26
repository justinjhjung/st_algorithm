from sys import stdin

def input():
    return stdin.readline().strip()

n, m = (int(x) for x in input().split())
T = []
A = []
B = []

for i in range(m):
    type, a, b = (int(x) for x in input().split())
    T.append(type); A.append(a); B.append(b);

class Solve:
    def __init__(self, n, m, T, A, B):
        self.n = n
        self.m = m
        self.T = T
        self.A = A
        self.B = B
        self.parent = [i for i in range(self.n+1)]

    def main(self):
        for i in range(self.m):
            if self.T[i] == 0:
                self.union(self.A[i], self.B[i])
            else:
                self.same(self.A[i], self.B[i])

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        # Adding big number under small number
        if root_a > root_b:
            self.parent[root_a] = root_b
        elif root_a < root_b:
            self.parent[root_b] = root_a

    def same(self, a, b):
        print("YES" if self.find(a) == self.find(b) else "NO")

solve = Solve(n, m, T, A, B)
solve.main()