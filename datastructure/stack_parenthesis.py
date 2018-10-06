from sys import stdin

def input():
    return stdin.readline().strip()

def solve(target):
    stack = []

    for i in target:
        if stack:
            if i == '(':
                stack.append(i)
            else:
                stack.pop()
        else:
            if i == ')':
                print("No")
                return
            else:
                stack.append(i)
    if stack:
        print("No")
    else:
        print("Yes")

test_num = int(input())
for i in range(test_num):
    target = str(input())
    solve(target)

