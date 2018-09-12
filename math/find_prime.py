input_num = int(input())
input_ = [int(x) for x in input().split()]

def prime_finder(input_):
    cnt = 0
    for i in input_:
        if i == 1:
            pass
        elif i == 2:
            cnt += 1
        else:
            early_stop = round(i**.5)
            j = 2
            while True:
                if i % j != 0:
                    if j < early_stop:
                        j += 1
                    elif j == early_stop:
                        cnt += 1
                        break
                else:
                    break

    return cnt

print(prime_finder(input_))
