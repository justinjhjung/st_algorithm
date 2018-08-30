input_ = int(input())

def up(n):
    if n == 1:
        return 10
    dp = [[0 for i in range(10)] for i in range(n+1)]
    dp[1] = [1,1,1,1,1,1,1,1,1,1]    
    if n > 1:
        for i in range(2,n+1):
            for j in range(10):
                dp[i][j] = sum(dp[i-1][:j+1])
    return sum(dp[n])

print(up(input_)%10007)
