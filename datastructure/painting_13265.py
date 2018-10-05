from sys import stdin

def input():
    return stdin.readline().strip()

def dfs(s, c):
    color[s] = c

    for i in range(len(adj_list[s])):
        if color[i] == c:
            return False
        elif color[i] == 0 and not dfs(adj_list[s][i],-c):
            return False


# def solve(n, m, adj_list):
#     for i in range(n):
#         if color[i] == 0:
#             if not dfs(i, 1):
#                 print("Impossible")
#     if i ==
#     print("Possible")



test_num = int(input())
for i in range(test_num):
    n, m = (int(x) for x in input().split())
    adj_list = [[] for i in range(n+1)]
    color = [0 for i in range(n+1)]
    color[0] = 1 # 초기 조건

    for j in range(m):
        u, v = (int(x) for x in input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)

    print(dfs(1,1))