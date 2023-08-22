from itertools import permutations
import copy
from heapq import heappush, heappop

def solution(k, n, reqs):
    answer = int(1e9)
    cases = []
    def case(cur, n, arr):
        if cur == k:
            if n == sum(arr):
                cases.append(copy.deepcopy(arr))
            return
        tmp = arr
        for i in range(1, n):
            arr[cur] = i
            case(cur+1, n, arr)
            arr = tmp
        return 
    if n == k: cases = [[1] * n]
    else: case(0, n, [0]*k)
    for case in cases:
        present = [[] for _ in range(k)]
        time = 0
        for start, during, num in reqs:
            if len(present[num-1]) < case[num-1]:
                heappush(present[num-1], start+during)
            else:
                end = heappop(present[num-1])
                if end > start: 
                    time += end-start
                    heappush(present[num-1], end+during)
                else: heappush(present[num-1], start+during)
        answer = min(answer, time)
    return answer