from collections import Counter
def solution(topping):
    answer = 0
    N = len(topping)
    철수 = Counter()
    동생 = Counter(topping)
    for i in range(N):
        철수.update([topping[i]])
        동생.subtract([topping[i]])
        if 동생[topping[i]] == 0: del 동생[topping[i]]
        if len(철수) == len(동생):
            answer += 1

    return answer