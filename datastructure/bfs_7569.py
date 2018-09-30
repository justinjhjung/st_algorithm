from sys import stdin
from collections import deque
def input():
    return stdin.readline().strip()

INF = 10000000
M, N, H = (int(x) for x in input().split())
maze = [[[0 for j in range(M)] for i in range(N)] for k in range(H)]
d = [[[INF for j in range(M)] for i in range(N)] for k in range(H)]
que = deque()
tomato = 0

for k in range(H):
    for i in range(N):
        for j, value in enumerate(input().split()):
            value = int(value)
            maze[k][i][j] = value
            if value != -1:
                tomato += 1
                if value == 1:
                    que.append((k, i, j))
                    d[k][i][j] = 0

def bfs(tomato, maze, que):
    res = 0
    while que:
        z, x, y = que.popleft()
        tomato -= 1
        directions = [(z+1, x, y), (z-1, x, y),
                      (z, x+1, y), (z, x-1, y),
                      (z, x, y+1), (z, x, y-1)]
        for k, i, j in directions:
            if k >= H or k < 0 or i >= N or i < 0 or j >= M or j < 0:
                continue
            if d[k][i][j] != INF or maze[k][i][j] == -1:
                continue
            d[k][i][j] = d[z][x][y] + 1
            res = max(d[k][i][j], res)
            que.append((k,i,j))

    if tomato > 0:
        return -1
    else:
        return res


print(bfs(tomato, maze, que))