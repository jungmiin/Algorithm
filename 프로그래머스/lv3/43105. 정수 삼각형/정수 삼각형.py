from collections import deque

def solution(triangle):
    dp = [list(0 for _ in range(len(triangle[t]))) for t in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    max_value = 0
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
            elif j < len(triangle[i])-1:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
            else:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j])
            max_value = max(max_value, dp[i][j])

    return max_value