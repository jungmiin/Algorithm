from itertools import permutations

def solution(k, n, reqs):
    answer = 0
    per = list(permutations(range(1, n+1), k))
    print(per)
    return answer