from sys import stdin

def input():
    return stdin.readline().strip()

S = str(input())
T = str(input())
len_s = len(S)
len_t = len(T)

dp = [[0 for i in range(len_t+1)] for i in range(2)]

for i in range(len_s):
    for j in range(len_t):
        if S[i] == T[j]:
            dp[1][j+1] = dp[0][j] + 1
        else:
            dp[1][j+1] = max(dp[0][j+1], dp[1][j])
    dp[0] = dp[1].copy()

print(dp[1][len_t])