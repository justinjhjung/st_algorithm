input_ = int(input())

def tile_1(n):
    memoize = [0 for i in range(input_+1)]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    memoize[1] = 1
    memoize[2] = 2
    if n > 2:
        for i in range(3, n+1):
            memoize[i] = memoize[i-1] + memoize[i-2]
    return memoize[n]

print(tile_1(input_)%10007)
