def solution(N, A):
    answer = [0 for _ in range(N)]
    tmp_max_value = 0
    all_max_value = 0
    
    for a in A:
        if a <= N:
            if answer[a-1] < all_max_value:
                answer[a-1] = all_max_value+1
            else: 
                answer[a-1] += 1
            tmp_max_value = max(tmp_max_value, answer[a-1])
        else:
            all_max_value = tmp_max_value
    
    def fill_max(n):
        if n < all_max_value:
            return all_max_value
        return n

    answer = list(map(fill_max, answer))

    return answer