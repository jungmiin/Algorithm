def solution(n):
    if n == 1 : return 1
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] += dp[i-1]
        dp[i] += dp[i-2]
    return dp[-1] % 1234567