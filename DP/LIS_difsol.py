from sys import stdin

def input():
    return stdin.readline().strip()

N = int(input())
a = [int(x) for x in input().split()]

res = 0
dp = [0 for i in range(N+1)]

for i in range(N):
    dp[i+1] = 1
    for j in range(i):
        if a[i] > a[j]:
            dp[i+1] = max(dp[i+1], dp[j+1] + 1)
    res = max(res, dp[i+1])
print(res)