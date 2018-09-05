test_num = int(input())

def padovan(input_):
    if input_ in [1,2,3]:
        return 1
        
    elif input_ in [4,5]:
        return 2
    
    dp = [0 for i in range(input_+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    
    if input_ > 5:
        for i in range(6,input_+1):
            dp[i] = dp[i-5] + dp[i-1]
    
    return dp[input_]
    
for i in range(test_num):
    input_ = int(input())
    print(padovan(input_))
