from sys import stdin

def input():
    return stdin.readline().strip()

def leastcoin(coins, change):
    res = 0
    for coin in coins:
        if coin > change:
            continue
        leastamnt = change//coin
        res += leastamnt
        change -= leastamnt * coin
    return res

test_num = int(input())
for i in range(test_num):
    coin_num = int(input())
    coins = [int(x) for x in input().split()][::-1]
    change = int(input())
    print(leastcoin(coins, change))