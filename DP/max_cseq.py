num = int(input())
inputs = [int(x) for x in input().split()]

def max_sum(num, inputs):
    if num == 1:
        return inputs[0]
    
    dp = [0 for i in range(num+1)]
    dp[1] = inputs[0]
    
    if num > 1:
        if len([i for i in inputs if i > 0]) == 0:
            return max(inputs)
        else:
            for i in range(2,num+1):
                dp[i] = max( dp[i-1] + inputs[i-1], inputs[i-1] )
    
    return max(dp[i] for i in range(1,num+1))
                
print(max_sum(num, inputs))
