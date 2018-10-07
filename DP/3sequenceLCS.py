from sys import stdin

def input():
    return stdin.readline().strip()

def LCS(x, y, z):
    len_x = len(x)
    len_y = len(y)
    len_z = len(z)
    dp = [[[0 for k in range(len_z + 1)] for j in range(len_y + 1)] for i in range(len_x + 1)]

    res = 0
    for i in range(len_x):
        for j in range(len_y):
            for k in range(len_z):
                if x[i] == y[j] and y[j] == z[k]:
                    dp[i + 1][j + 1][k + 1] = dp[i][j][k] + 1
                else:
                    dp[i + 1][j + 1][k + 1] = max(dp[i+1][j][k],
                                                  dp[i+1][j][k+1],
                                                  dp[i+1][j+1][k],
                                                  dp[i][j+1][k+1],
                                                  dp[i][j+1][k],
                                                  dp[i][j][k+1])
            res = max(res, dp[i + 1][j + 1][k + 1])
    return res

test_num = int(input())
for i in range(test_num):
    a = str(input())
    b = str(input())
    c = str(input())
    print(LCS(a,b,c))