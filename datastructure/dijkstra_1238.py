from sys import stdin
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, prio, idx):
        heapq.heappush(self.heap, (prio, idx))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def __len__(self):
        return len(self.heap)

def input():
    return stdin.readline().strip()

N, M, X = (int(x) for x in input().split())
INF = 10000000
adj_list = [[] for i in range(N+1)]
rev_adj_list = [[] for i in range(N+1)]

# Creating adjacent list
for i in range(M):
    u, v, w = (int(x) for x in input().split())
    adj_list[u].append((v,w))
    rev_adj_list[v].append((u,w))

# Main
def dist_calc(adjlist):
    checked = [True] + [False] * N
    dist = [INF] * (N+1)
    q = MinHeap()
    q.push(0, X)
    dist[X] = 0
    while q:
        min_idx = q.pop()
        if checked[min_idx]:
            continue
        checked[min_idx] = True
        for v, w in adjlist[min_idx]:
            dist[v] = min(dist[v], dist[min_idx]+w)
            print(dist[v], dist[min_idx], v)
            q.push(dist[v],v)
    return dist[1:]

print(max(i+j for (i,j) in zip(dist_calc(adj_list), dist_calc(rev_adj_list))))

