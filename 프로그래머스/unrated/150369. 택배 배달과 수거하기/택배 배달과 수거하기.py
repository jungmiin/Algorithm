# 그리디 같음
# 최대한 멀리서부터, 최대한 꽉 채워서
def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    for i in range(-1, -n-1, -1):
        d += deliveries[i]
        p += pickups[i]
        while d > 0 or p > 0:
            answer += (n+i+1)*2
            d -= cap
            p -= cap
    return answer