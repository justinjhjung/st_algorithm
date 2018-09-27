from sys import stdin

def input():
    return stdin.readline().strip()

N = int(input())
P = []
for i in range(N):
    start, end = (int(x) for x in input().split())
    P.append((start,end))

def solve(N, P):
    P = sorted(P, key=lambda x: (x[1], x[0]))
    ans = 0
    pos = 0

    for interval in P:
        if pos <= interval[0]:
            ans += 1
            pos = interval[1]
    return ans

print(solve(N, P))