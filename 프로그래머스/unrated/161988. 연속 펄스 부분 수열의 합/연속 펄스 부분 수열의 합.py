def solution(sequence):
    answer = 0
    INF = -int(1e9)
    dp = [[INF]*(len(sequence)+1) for _ in range(2)]
    pulse = -1
    dp[0][0], dp[1][0] = 0, 0
    for i in range(1, len(sequence)+1):
        dp[0][i] = max(sequence[i-1]*pulse, dp[0][i-1]+sequence[i-1]*pulse)
        dp[1][i] = max(sequence[i-1]*(-pulse), dp[1][i-1]+sequence[i-1]*(-pulse))
        pulse *= -1
    # print(dp)
    return max(max(dp[0]), max(dp[1]))