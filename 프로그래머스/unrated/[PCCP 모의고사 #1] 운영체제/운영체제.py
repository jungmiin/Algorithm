from heapq import heappush, heappop
from collections import deque
def solution(programs):
    N = len(programs)
    wait_time = 0
    wait_time_by_score = [0] * 11
    queue, now, idx = [], 0, 0
    programs = deque(sorted(programs, key=lambda x: x[1]))
    while idx < N:
        while programs and programs[0][1] <= now:
            score, called_time, execution_time = programs.popleft()
            heappush(queue, (score, called_time, execution_time))
        if queue:
            score, called_time, execution_time = heappop(queue)
            wait_time_by_score[score] += now-called_time
            now += execution_time
            idx += 1 
        else :
            now += 1 
    return [now] + wait_time_by_score[1:]