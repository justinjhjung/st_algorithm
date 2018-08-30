input_ = int(input())

def making_one(n):
    memoize = [10000 for i in range(n+1)]
    if n == 1:
        return 0
    
    memoize[1] = 0
    memoize[2] = 1
    for i in range(3, n + 1):
        if i % 3 == 0:
            if i % 2 == 0:
                memoize[i] = min(memoize[i//3], memoize[i//2], memoize[i - 1]) + 1
            else:
                memoize[i] = min(memoize[i//3], memoize[i - 1]) + 1
        elif i % 2 == 0:
            memoize[i] = min(memoize[i//2], memoize[i - 1]) + 1
        else:
            memoize[i] = memoize[i - 1] + 1
    return memoize[n]

print(making_one(input_))
