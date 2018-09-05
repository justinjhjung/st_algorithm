input_ = int(input())

def min_squarepowers(input_):
    if input_ == 1:
        return 1
    
    dp = [0 for i in range(input_+1)]
    dp[1] = 1
    
    if input_ > 1:
        for i in range(2,input_+1):
            root = int(i**.5)
            dp[i] = min(dp[i-j**2] for j in range(1,root+1)) + 1
    
    return dp[input_]

print(min_squarepowers(input_))
