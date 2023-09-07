def solution(e, starts):
    answer = []
    cache_num = 0
    cache_cnt = 0
    dp = [0] * (e+1)
    
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            dp[j] += 1
            
    for n in range(e, 0, -1):
        if dp[n] >= cache_cnt:
            cache_num = n
            cache_cnt = dp[n]
        dp[n] = cache_num     
            
    return [dp[start] for start in starts]