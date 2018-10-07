from sys import stdin
import heapq

def input():
    return stdin.readline().strip()

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, prio, item):
        heapq.heappush(self.heap, (prio, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def __len__(self):
        return len(self.heap)

INF = 2147483660
V, E = (int(x) for x in input().split())
adj_list = [[] for i in range(V+1)]
d = [INF for i in range(V+1)]
visited = [False for i in range(V+1)]
for i in range(E):
    u, v, w = (int(x) for x in input().split())
    adj_list[u].append((w,v))
    adj_list[v].append((w,u))

que = MinHeap()
start = 1
que.push(0,1)
d[1] = 0

while que:
    min_idx = que.pop()
    if visited[min_idx]:
        continue
    visited[min_idx] = True
    for w, u in adj_list[min_idx]:
        if d[u] > w and not visited[u]:
            d[u] = w
            que.push(w,u)
print(sum(d[1:]))


