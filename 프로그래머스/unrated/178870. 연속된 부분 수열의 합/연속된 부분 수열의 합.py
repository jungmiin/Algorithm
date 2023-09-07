def solution(sequence, k):
    answer = []
    right = 0
    sequence_sum = sequence[0]
    for left in range(len(sequence)):
        while right + 1 < len(sequence) and sequence_sum < k:
            right += 1
            sequence_sum += sequence[right]
        if sequence_sum == k:
            if not answer:
                answer = [left, right]
            else:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]
        sequence_sum -= sequence[left]
    return answer