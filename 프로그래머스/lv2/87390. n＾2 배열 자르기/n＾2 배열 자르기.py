def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = max(i//n, i%n) + 1
        answer.append(v)
    return answer