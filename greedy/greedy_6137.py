from sys import stdin

def input():
    return stdin.readline().strip()

N = int(input())
S = ""
for i in range(N):
    S += str(input())


def solve(N, S):
    a = 0
    b = N-1
    ans = ''
    while a <= b:
        sub_s = S[a:b+1]
        if sub_s < sub_s[::-1]:
            ans += S[a]
            a += 1
        else:
            ans += S[b]
            b -= 1
    return ans

T = solve(N, S)
print('\n'.join(T[i:i+80] for i in range(0,N,80)))
