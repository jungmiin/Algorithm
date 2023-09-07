# 실외 온도, 실내 온도 범위, 에어컨 소비 전력(다를때, 같을 때), 탑승 중인 시간
def solution(temperature, t1, t2, a, b, onboard):
    temperature += 11
    t1 += 11
    t2 += 11
    INF = int(1e9)
    N = len(onboard)
    start = min(t1, temperature)
    end = max(t2, temperature)
    dp = [ [INF]*53 for _ in range(N) ]
    
    
    dp[0][temperature] = 0
        
    for i in range(1, N):
        start = 0
        end = 0
        if onboard[i]:
            start = t1
            end = t2
        else:
            start = min(t1, temperature)
            end = max(t2, temperature)
        for j in range(start, end+1):
            l = dp[i - 1][j - 1] if j-1 < temperature else dp[i - 1][j - 1] + a
            m = dp[i - 1][j] if j == temperature else dp[i - 1][j] + b
            h = dp[i - 1][j + 1] if j+1 > temperature else dp[i - 1][j + 1] + a

            dp[i][j] = min(l, m, h)
    return min(dp[N-1])