def cut_the_rod(input_):
    rod = 0
    cnt = 0
    laser = 0
    stack = []

    for idx, i in enumerate(input_):
        if i == '(':
            rod += 1
            stack.append(i)
        else:
            rod -= 1
            if input_[idx - 1] == '(':
                laser = 1
                num = laser * rod
                cnt += num
                stack.pop(-1)
            else:
                cnt += 1

    return cnt

if __name__ == '__main__':
    res1 = cut_the_rod("()(((()())(())()))(())") == 17
    res2 = cut_the_rod("(((()(()()))(())()))(()())") == 24
    if (res1 == True) & (res2 == True):
        print("Correct!!")