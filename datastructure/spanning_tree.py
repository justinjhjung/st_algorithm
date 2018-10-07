import heapq
class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, prio, item):
        heapq.heappush(self.heap, (prio, item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def __len__(self):
        return len(self.heap)


from sys import stdin

def input():
    return stdin.readline().strip()


V = int(input())
E = int(input())

adj_list = [[] for  i in range(V+1)]

for i in range(E):
    u, v, w = (int(x) for x in input().split(" "))
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

INF = 999999999
checked = [True] + [False for i in range(V)]
dist = [INF] * (V+1)
dist[1] = 0
q = MinHeap()
q.push(0, 1)

while q:
    min_idx = q.pop()
    if checked[min_idx] == True:
       continue
    checked[min_idx] = True
    for v, w in adj_list[min_idx]:
        if dist[v] > w and not checked[v]:
            dist[v] = w
        else:
            continue
        q.push(dist[v], v)

print(sum(dist[1:]))