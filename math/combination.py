from sys import stdin

def input():
    return stdin.readline().strip()

n, m = (int(x) for x in input().split())

# down-top approach
def combination(n, m):
    if m == 0 or n == 1:
        return 1
    dp = [[1 if j==0 or j==i else i if j==1 else 0 for j in range(m+1)] for i in range(n+1)]

    for i in range(2,n+1):
        for j in range(1,m+1):
            if j > i:
                continue
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][m]

print(combination(n, m))

# top-down approach
def combination(n, m):
    if m == 0 or n == 1 or n == m:
        return 1

    if m == 1:
        return n

    return combination(n-1,m) + combination(n-1,m-1)

print(combination(n, m))


