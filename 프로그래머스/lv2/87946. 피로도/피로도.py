from itertools import permutations

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    perms = list(permutations([i for i in range(n)], n))
    for perm in perms:
        tmp_k = k
        tmp_answer = 0
        for p in perm:
            if dungeons[p][0] > tmp_k:
                is_possible = False
                break
            else:
                tmp_answer += 1
                tmp_k -= dungeons[p][1]
        if tmp_answer == n:
            return tmp_answer
        else: 
            answer = max(answer, tmp_answer)
    return answer