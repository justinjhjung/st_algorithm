# Longest Common Substring (연속하는 공통 부분 문자열)
from sys import stdin

def input():
    return stdin.readline().strip()

S = str(input())
T = str(input())
len_s = len(S)
len_t = len(T)

dp = [[0 for j in range(len_t+1)] for i in range(len_s+1)]

max_ = 0
for i in range(len_s):
    for j in range(len_t):
        if S[i] == T[j]:
            dp[i+1][j+1] = dp[i][j] + 1

        # Difference with Longest common subsequence is that
        # we don't do anything with the occasion where S[i] != T[i].
        # Then dp[i+1][j+1] stays 0, which would function as
        # "Renewal" of the substring that follows.

        # Below is the renewal of max_substring length.
        if dp[i+1][j+1] > max_:
            max_ = dp[i+1][j+1]

print(max_)