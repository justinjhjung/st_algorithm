input_ = int(input())

def echinsoo(n):
    if n == 1:
        return 1
    dp = [[0 for i in range(2)] for i in range(n+1)]
    dp[1] = [0,1]
    
    if n > 1:
        for i in range(2,n+1):
            dp[i][0] = dp[i-1][1] + dp[i-1][0]
            dp[i][1] = dp[i-1][0]
    return sum(dp[n])

print(echinsoo(input_))
