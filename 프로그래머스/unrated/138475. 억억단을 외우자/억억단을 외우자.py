def solution(e, starts):
    divisors = [0 for _ in range(e + 1)]
    for i in range(1, e + 1):
        for j in range(i, e + 1):
            if (temp := i * j) > e:
                break
            divisors[temp] += 1 if i == j else 2
    max_num = 0
    for index in range(e, 0, -1):
        if divisors[index] >= max_num:
            max_num = divisors[index]
            divisors[index] = index
        else:
            divisors[index] = divisors[index + 1] 
    return [divisors[start] for start in starts]