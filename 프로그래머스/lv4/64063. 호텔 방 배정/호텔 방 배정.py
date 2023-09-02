import sys
sys.setrecursionlimit(10**6)
def solution(k, room_number):
    answer = []
    next = dict()
    
    def find(x):
        if not next.get(x):
            next[x] = x+1
            return x
        else: 
            next[x] = find(next[x])
            return next[x]

    for number in room_number:
        answer.append(find(number))

    return answer