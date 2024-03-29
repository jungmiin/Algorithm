# 동전 1

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
dp = [0 for _ in range(k+1)] 

dp[0] = 1

for coin in coins:
    for i in range(1, k+1):
        if i>=coin:
            dp[i] += dp[i-coin]

print(dp[k])