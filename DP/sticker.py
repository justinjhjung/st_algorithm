test_num = int(input())

def max_score(col_num, row_0, row_1):
    if col_num == 1:
        return max(row_0[0], row_1[0])
    
    dp = [[0 for i in range(3)] for i in range(col_num+1)]
    dp[1] = [row_0[0], row_1[0], 0]
    
    if col_num > 1:
        for i in range(2,col_num+1):
            dp[i][0] = max(dp[i-1][1] + row_0[i-1], dp[i-1][2] + row_0[i-1])
            dp[i][1] = max(dp[i-1][0] + row_1[i-1], dp[i-1][2] + row_1[i-1])
            dp[i][2] = max(dp[i-1][1], dp[i-1][0])
    
    return max(dp[col_num])

for i in range(test_num):
    col_num = int(input())
    row_0 = [int(x) for x in input().split()]
    row_1 = [int(x) for x in input().split()]
    
    print(max_score(col_num, row_0, row_1))
