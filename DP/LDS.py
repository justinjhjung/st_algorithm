num = int(input())
inputs = [int(x) for x in input().split()]

def LDS(num, inputs):
    if num == 1:
        return 1
    # 부분 수열의 길이, 해당 부분수열의 마지막 수
    dp = [[0 for i in range(2)] for i in range(num+1)]
    dp[1] = [1, inputs[0]]
    
    if num > 1:
        for i in range(2, num+1):
            temp = []
            for j in range(1,i):
                if dp[j][1] > inputs[i-1]:
                    temp.append(dp[j][0])
                    
            if inputs[i-1] > max(dp[j][1] for j in range(1,i)):
                    dp[i] = [1, inputs[i-1]]
            
            if len(temp) == 0:
                pass
            else:
                dp[i][0] = max(temp) + 1
                dp[i][1] = inputs[i-1]

    return max(dp[i][0] for i in range(num+1))

print(LDS(num, inputs))
