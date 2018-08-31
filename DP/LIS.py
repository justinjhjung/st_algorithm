num = int(input())
inputs = [int(x) for x in input().split()]

def LIS(num, inputs):
    if num == 1:
        return 1
    # 부분 수열의 길이, 해당 부분수열의 마지막 수
    dp = [[0 for i in range(2)] for i in range(num+1)]
    dp[1] = [1, inputs[0]]
    
    if num > 1:
        for i in range(2, num+1):
            temp = []
            for j in range(1,i):
                if dp[j][1] < inputs[i-1]:
                    temp.append(dp[j][0])
            
            # 10 50 20 5 10 11 12 13 20 30 이런 경우를 대비해서 만든 조건
            if inputs[i-1] < min(dp[j][1] for j in range(1,i)):
                    dp[i] = [1, inputs[i-1]]
            
            # 앞에 있는 수들이 현재 수(dp[i][1]보다 크거나 같은 경우 temp에 아무것도 들어가지 않게 됨. 그럼 max()가 작동이 안 됨. 
            if len(temp) == 0:
                pass
            else:
                dp[i][0] = max(temp) + 1
                dp[i][1] = inputs[i-1]
                
    # 마지막에 max를 굳이 넣은 이유는 10 20 10 30 50 70 20 50 이렇게 끝나는 것을 대비
    return max(dp[i][0] for i in range(num+1))

print(LIS(num, inputs))
