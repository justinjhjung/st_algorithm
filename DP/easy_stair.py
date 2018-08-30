input_ = int(input())

def stair_num(n):
    if n == 1:
        return 9
    dp = [[0 for i in range(10)] for i in range(n+1)]
    dp[1] = [0,1,1,1,1,1,1,1,1,1]
    
    if n > 1:
        for i in range(2,n+1):
            dp[i][0] = dp[i-1][1]
            dp[i][9] = dp[i-1][8]
            for j in range(1,9):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    return sum(dp[n])

print(stair_num(input_)%1000000000)
