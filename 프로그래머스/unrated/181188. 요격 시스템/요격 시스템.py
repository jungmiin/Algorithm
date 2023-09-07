# 이진 탐색...? 

def solution(targets):
    answer = 0
    scope = 0
    for s, e in sorted(targets):
        if scope > s:
            scope = min(scope, e)
        else:
            answer += 1
            scope = e
    return answer