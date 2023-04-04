from collections import deque
def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    for i in range(300000):
        if sum1 == sum2:
            return i
        elif sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        elif sum2 > sum1:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
    return -1
            