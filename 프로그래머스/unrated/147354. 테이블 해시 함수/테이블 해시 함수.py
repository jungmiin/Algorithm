def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin-1, row_end):
        S_i = 0
        for d in sorted_data[i]:
            S_i += d % (i+1)
        answer ^= S_i
    return answer