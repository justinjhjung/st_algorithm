input_ = int(input())

def tile_3(input_):
    if input_ %2 == 1:
        return 0
    elif input_ == 0:
        return 1
    elif input_ == 2:
        return 3
    
    dp = [0 for i in range(input_+1)]
    dp[0] = 1
    dp[2] = 3
    
    if input_ > 2:
        for i in range(4,input_+1,2):
            dp[i] += 3 * dp[i-2]
            for j in range(4,i+1,2):
                dp[i] += 2 * dp[i-j]
    
    return dp[input_]
    
print(tile_3(input_))
