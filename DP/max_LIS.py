num = int(input())
inputs = [int(x) for x in input().split()]

def max_LIS(num, inputs):
    if num == 1:
        return inputs[0]
    
    dp = [[0 for i in range(2)] for i in range(num+1)]
    dp[1] = [inputs[0], inputs[0]]
    
    if num > 1:
        for i in range(2,num+1):
            temp = []
            for j in range(1,i):
                if dp[j][1] < inputs[i-1]:
                    temp.append(dp[j][0])

            if inputs[i-1] < min(dp[j][1] for j in range(1,i)):
                dp[i] = [inputs[i-1], inputs[i-1]]

            if len(temp) == 0:
                pass
            else:
                dp[i][0] = max(temp) + inputs[i-1]
                dp[i][1] = inputs[i-1]
        
    return max(dp[i][0] for i in range(num+1))

print(max_LIS(num, inputs))
