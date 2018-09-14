input_ = int(input())

def factorial(input_):
    mul = 1
    for i in range(2,input_+1):
        mul *= i
    return mul

def count(factorial_):
    as_string = str(factorial_)
    cnt = 0
    i = 0
    while True:
        if as_string[::-1][i] == '0':
            i += 1
            cnt += 1
        else:
            break
    return cnt

res = factorial(input_)
print(count(res))
