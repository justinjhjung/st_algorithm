input_ = str(input())
length = len(input_)

def possibility(length, input_):
    if input_[0] == '0':
        return 0
    if length == 1:
        return 1
    
    dp = [0 for i in range(length+1)]
    dp[0] = 1
    dp[1] = 1
    
    if length > 1:
        for i in range(2,length+1):
            if input_[i-1] == '0':
                if input_[i-2] in ['1','2']:
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                num = int(input_[i-2])*10 + int(input_[i-1])
                if (num >= 10) and (num <= 26):
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
    
    return dp[length]
    
    
print(possibility(length, input_)%1000000)
