N, K = (int(x) for x in input().split())

def add_decomposition(N, K):
    if K == 1:
        return 1
    
    # 각 숫자(N)마다 1~K개씩으로 더 할 수 있는데, 그때의 경우의 수를 각 k자리에 저장
    dp = [[0 for i in range(K+1)] for i in range(N+1)]
    dp[1] = [i for i in range(K+1)]
    
    if K > 1:
        for i in range(2,N+1):
            dp[i][0] = 0
            dp[i][1] = 1
            for j in range(2,K+1):
                dp[i][j] = sum(dp[i-1][k] for k in range(1,j+1))
    
    return dp[N][K]
    
print(add_decomposition(N, K)%1000000000)
