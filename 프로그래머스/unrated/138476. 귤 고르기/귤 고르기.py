from collections import Counter, deque
def solution(k, tangerine):
    answer = 0
    N = len(tangerine)
    counter = deque(sorted(Counter(tangerine).items(), key=lambda x: (x[1], x[0])))
    tmp = N
    while tmp > k:
        size, num = counter.popleft()
        if tmp - num < k:
            return len(counter)+1
        tmp -= num
    return len(counter)