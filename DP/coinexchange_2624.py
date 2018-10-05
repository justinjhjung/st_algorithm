from sys import stdin

def input():
    return stdin.readline().strip()

T = int(input())
k = int(input())
B = []

for i in range(k):
    p, n = (int(x) for x in input().split())
    B.append((p,n))

B = sorted(B, key=lambda x: x[0])

dp = [[0 for j in range(k)] for i in range(T+1)]

for i in range(T+1):
    for j in range(k):
        dp[0][j-1] = 1
        p = B[j][0]
        n = B[j][1]
        t = 0
        while i >= t * p and t <= n:
            dp[i][j] += dp[i - t * p][j - 1]
            t += 1

print(dp[T][k-1])








