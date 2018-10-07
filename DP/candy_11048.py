from sys import stdin

def input():
    return stdin.readline().strip()

N, M = (int(x) for x in input().split())

candy = [[int(j) for j in input().split()] for i in range(N)]
dp = [[0 for j in range(M)] for i in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = candy[i][j] + max(dp[i-1][j-1] if i > 0 and j > 0 else 0,
                                     dp[i-1][j] if i > 0 else 0,
                                     dp[i][j-1] if j > 0 else 0)

print(dp[N-1][M-1])
