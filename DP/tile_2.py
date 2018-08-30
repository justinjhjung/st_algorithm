input_ = int(input())

def tile_2(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    memoize = [0 for i in range(input_+1)]
    memoize[1] = 1
    memoize[2] = 3
    if n > 2:
        for i in range(3, n+1):
            memoize[i] = memoize[i-1] + 2 * memoize[i-2]
    return memoize[n]

print(tile_2(input_)%10007)
