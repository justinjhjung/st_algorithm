num = int(input())
inputs = [int(x) for x in input().split()]

def LBS(num, inputs):
    if num == 1:
        return 1
    reverse = inputs[::-1]
    # 길이, 마지막 수
    LIS_left_dp = [[0 for i in range(2)] for i in range(num+1)]
    LIS_right_dp = [[0 for i in range(2)] for i in range(num+1)]
    num = int(input())
inputs = [int(x) for x in input().split()]

def LBS(num, inputs):
    if num == 1:
        return 1
    reverse = inputs[::-1]
    # 길이, 마지막 수
    LIS_left_dp = [[0 for i in range(2)] for i in range(num+1)]
    LIS_right_dp = [[0 for i in range(2)] for i in range(num+1)]
    
    LIS_left_dp[1] = [1, inputs[0]]
    LIS_right_dp[1] = [1, reverse[0]]
    
    if num > 1:
        for i in range(2, num+1):
            temp_left = []
            temp_right = []
            for j in range(1,i):
                if LIS_left_dp[j][1] < inputs[i-1]:
                    temp_left.append(LIS_left_dp[j][0])
                if LIS_right_dp[j][1] < reverse[i-1]:
                    temp_right.append(LIS_right_dp[j][0])
            
            if inputs[i-1] < min(LIS_left_dp[j][1] for j in range(1,i)):
                LIS_left_dp[i] = [1, inputs[i-1]]
            if reverse[i-1] < min(LIS_right_dp[j][1] for j in range(1,i)):
                LIS_right_dp[i] = [1, reverse[i-1]]
            
            if len(temp_left) != 0:
                LIS_left_dp[i][0] = max(temp_left) + 1
                LIS_left_dp[i][1] = inputs[i-1]
            if len(temp_right) != 0:
                LIS_right_dp[i][0] = max(temp_right) + 1
                LIS_right_dp[i][1] = reverse[i-1]
    
    return max(LIS_left_dp[i][0]+LIS_right_dp[num+1-i][0]-1 for i in range(1,num+1))

print(LBS(num, inputs))
