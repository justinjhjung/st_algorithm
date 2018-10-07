from sys import stdin
import heapq

def input():
    return stdin.readline().strip()

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, prio, idx):
        heapq.heappush(self.heap, (prio, idx))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def __len__(self):
        return len(self.heap)

INF = 1000000000
test_num = int(input())
for i in range(test_num):
    V = int(input())
    visited = [False] * (V+1)
    dist = [INF] * (V+1)
    C = [int(x) for x in input().split()]
    C = [0] + C
    path_num = int(input())
    que = MinHeap()
    que.push(0,1)
    dist[1] = C[1]

    adj_list = [[] for i in range(V+1)]
    for i in range(path_num):
        u, v = (int(x) for x in input().split())
        adj_list[u].append((C[v],v))
        adj_list[v].append((C[u],u))

    if len(adj_list[V]) < 1:
        print(-1)

    else:
        while que:
            min_idx = que.pop()

            if visited[min_idx]:
                continue
            visited[min_idx] = True
            print(dist)
            print(visited)
            for w, v in adj_list[min_idx]:
                if not visited[v]:
                    dist[v] = min(dist[v], dist[min_idx]+w)
                    que.push(dist[v], v)
    
    if dist[V] >= INF:
        print(-1)
    else:
        print(dist[V]-C[V])