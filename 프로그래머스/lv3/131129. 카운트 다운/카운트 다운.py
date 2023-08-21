def solution(target):
    answer = []
    single_or_fire = 0
    INF = int(1e9)
    dp = [[INF, 0] for _ in range(target+1)]
    
    for i in range(1, 21):
        if len(dp) > i: 
            dp[i] = [1, 1]
        if len(dp) > i*2:
            dp[i*2] = [1, 0]
        if len(dp) > i*3:
            dp[i*3] = [1, 0]
    if len(dp) > 50: 
        dp[50] = [1, 1]
    
    for i in range(21, target+1):
        if i > 60:
            dp[i][0] = min(dp[i][0], dp[i-60][0]+1)
            dp[i][1] = dp[i-60][1]
        if dp[i][0] >= dp[i-20][0]+1:
            dp[i][0] = min(dp[i][0], dp[i-20][0]+1)
            dp[i][1] = dp[i-20][1] + 1
        if i > 50 and dp[i][0] >= dp[i-50][0]+1:
            dp[i][0] = min(dp[i][0], dp[i-50][0]+1)
            dp[i][1] = dp[i-50][1] + 1
    # for i in range(len(dp)):
    #     print(i,":", dp[i])
    return dp[target]