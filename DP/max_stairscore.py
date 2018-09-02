num = int(input())

inputs = []
for i in range(num):
    input_ = int(input())
    inputs.append(input_)
    
def max_stairscore(num, inputs):
    if num == 1:
        return inputs[0]
    
    # 0번 연속, 1번 연속, 2번 연속일 때의 합
    dp = [[0 for i in range(3)] for i in range(num+1)]
    dp[1] = [0, inputs[0], 0]
    
    if num > 1:
        for i in range(2,num+1):
            dp[i][0] = max( dp[i-1][1], dp[i-1][2] )
            dp[i][1] = dp[i-1][0] + inputs[i-1]
            dp[i][2] = dp[i-1][1] + inputs[i-1]
    
    # 마지막 스텝에서 0인 것(밟지 않는 것)은 가능하지 않으므로 dp[num][1], dp[num][2]만 고려되어야 함
    return max(dp[num][j] for j in range(1,3))
    
    
print(max_stairscore(num, inputs))
