num = int(input())

def max_consumption(num, inputs):
    if num < 3:
        return sum(inputs[:num])
    
    dp = [[0 for i in range(3)] for i in range(num+1)]
    # 0번 연속, 1번 연속, 2번 연속
    dp[1] = [0, inputs[0], 0]
    
    if num >= 3:
        for i in range(2,num+1):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + inputs[i-1]
            dp[i][2] = dp[i-1][1] + inputs[i-1]
    return max(dp[num])

inputs = []
for i in range(num):
    inputs.append(int(input()))

print(max_consumption(num, inputs))
