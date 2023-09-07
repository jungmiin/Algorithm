def solution(queries):
    answer = []
    res = ["", "RR", "Rr", "Rr", "rr"]
    for n, p in queries:
        if n == 1:
            answer.append("Rr")
            continue
        tmp = p
        for i in range(n-1, 0, -1):
            if i == 1:
                answer.append(res[tmp])
                break
            else:
                if tmp <= 4**(i-1):
                    answer.append("RR")
                    break
                elif tmp > 4**(i-1)*3:
                    answer.append("rr")
                    break
                tmp %= 4**(i-1)
                if tmp == 0: tmp = 4**(i-1)
    return answer