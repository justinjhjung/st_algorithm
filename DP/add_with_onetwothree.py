test_num = int(input())

def adder(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    memoize = [0 for i in range(input_+1)]
    memoize[1] = 1
    memoize[2] = 2
    memoize[3] = 4
    
    if n > 2:
        for i in range(4, n+1):
            memoize[i] = memoize[i-1] + memoize[i-2] + memoize[i-3]
    return memoize[n]

for i in range(test_num):
    input_ = int(input())
    print(adder(input_))
