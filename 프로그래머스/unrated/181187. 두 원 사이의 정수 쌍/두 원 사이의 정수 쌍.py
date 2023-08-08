import math

def solution(r1, r2):
    answer = 0
    for y in range(1, r2+1):
        big_x = math.floor((r2**2-y**2)**0.5)
        small_x = math.ceil((r1**2-y**2)**0.5) if (r1**2-y**2) > 0 else 0
        answer += (big_x - small_x) + 1 if big_x > small_x else 1
    return answer*4