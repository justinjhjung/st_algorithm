test_num = int(input())
def GCD(a, b):
    small = min(a, b)
    large = max(a, b)
    
    if small == 0:
        return 0
    elif small == 1:
        return 1
    
    dp = [10000000 for i in range(large+1)]
    dp[0] = large
    dp[1] = small
    
    for i in range(2,large+1):
        current = dp[i-2]%dp[i-1]
        if current != 0:
            dp[i] = current
        else:
            break
            
    return min(dp)

def LCM(a, b):
    gcd = GCD(a, b)
    return a*b//gcd

for i in range(test_num):
    a, b = (int(x) for x in input().split())
    print(LCM(a,b))
