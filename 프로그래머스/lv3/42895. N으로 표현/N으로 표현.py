def solution(N, number):
    answer = 0
    dp = []
    for i in range(1, 9):
        dp_set = set()
        dp_set.add(int(str(N)*i))
        if i > 1:
            for j in range(0, i-1):
                for k in dp[j]:
                    for l in dp[-j-1]:
                        dp_set.add(k * l)
                        dp_set.add(k - l)
                        dp_set.add(k + l)
                        if l > 0:
                            dp_set.add(int(k / l))
        if number in dp_set:
            return i
        dp.append(dp_set)
    return -1