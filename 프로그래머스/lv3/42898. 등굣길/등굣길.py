def solution(m, n, puddles):
    dp= [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for r, c in puddles:
        dp[r-1][c-1] = -1
    for i in range(m):
        for j in range(n):
            if dp[i][j] == -1: continue
            if i > 0 and dp[i-1][j] != -1: dp[i][j] += dp[i-1][j]
            if j > 0 and dp[i][j-1] != -1: dp[i][j] += dp[i][j-1]
    return dp[-1][-1] % 1000000007