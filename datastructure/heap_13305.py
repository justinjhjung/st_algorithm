from sys import stdin
import heapq

def input():
    return stdin.readline().strip()

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, x)

    def pop(self):
        return heapq.heappop(self.heap)[0]

    def top(self):
        return self.heap[0]

N = int(input())
A = [int(x) for x in input().split()]
price = [int(x) for x in input().split()]

def solve(N,A,price):
    ans = 0
    que = MinHeap()
    # We don't have to care about the last city's oil price,
    # hence, we can loop until the path ends. ( the number of path = max city number - 1)
    for i in range(N-1):
        # push the oil price of the current city
        que.push(price[i])
        # take the minimum price and multiply the path length
        ans += A[i] * que.top()
    return ans

print(solve(N,A,price))

