from sys import stdin
from collections import deque

def input():
    return stdin.readline().strip()

M, N = (int(x) for x in input().split())
maze = [[0 for j in range(M)] for i in range(N)]
INF = 1000000000
d = [[INF for j in range(M)] for i in range(N)]
que = deque()
tomato = 0
for i in range(N):
    for j, value in enumerate(input().split()):
        value = int(value)
        maze[i][j] += value
        if value == -1:
            continue
        else:
            tomato += 1
            if value == 1:
                que.append((i,j))
                d[i][j] = 0



def bfs(tomato, que, maze):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while que:
        if tomato < 1:
            break
        else:
            P = que.popleft()
            tomato -= 1
            for i in range(4):
                nx = P[0] + dx[i]
                ny = P[1] + dy[i]

                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                if maze[nx][ny] < 0 or d[nx][ny] != INF:
                    continue
                d[nx][ny] = d[P[0]][P[1]] + 1
                que.append((nx, ny))

    res = 0
    for line in d:
        for element in line:
            if element != INF:
                if res < element:
                    res = element

    if tomato != 0:
        print("-1")
    else:
        print(res)

bfs(tomato, que, maze)