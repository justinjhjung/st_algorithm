num = int(input())
inputs = [int(x) for x in input().split()]

def maxsale(n, inputs):
    if n == 1:
        return inputs[0]
    
    memoize = [0 for i in range(n+1)]
    memoize[1] = inputs[0]
    
    if n > 1:
        for i in range(2, n+1):
            temp = []
            for j in range(1,i+1):
                temp.append(memoize[i-j]+inputs[j-1])
            memoize[i] = max(temp)
    return memoize[n]

print(maxsale(num, inputs))
