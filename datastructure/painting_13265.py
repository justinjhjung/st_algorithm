from sys import stdin

def input():
    return stdin.readline().strip()

def dfs(stack, start):
    if len(stack) == 0:
        stack.append(start)
        color[start] = 1
    while stack:
        vertex = stack.pop()
        if visited[vertex]:
           continue
        visited[vertex] = True
        adjvertex = [i for i in adj_list[vertex] if not visited[i]]

        stack.extend(adjvertex)

        for i in adjvertex:
            if color[i] != 0:
                if (color[vertex] == color[i]):
                    return False
            else:
                color[i] = -color[vertex]

    return True

def solve(visited):
    stack = []
    for i in range(1,n+1):
        if visited == [True] * (n+1):
            print("possible")
            return
        if visited[i]:
            continue
        if not dfs(stack, i):
            print("impossible")
            return

test_num = int(input())
for i in range(test_num):
    n, m = (int(x) for x in input().split())
    adj_list = [[] for i in range(n+1)]
    color = [0 for i in range(n+1)]
    for j in range(m):
        u, v = (int(x) for x in input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = [True] + [False] * n
    solve(visited)