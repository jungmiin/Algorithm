

def solution(gems):
    types = list(set(gems))
    types_len = len(types)
    gems_len = len(gems)
    if types_len == gems_len:
        return [1, gems_len]
    elif len(types) == 1: return [1, 1]
    result = []
    def two_pointer(start, end, answer):
        right = list(set(gems[start+1:end]))
        left = list(set(gems[start:end-1]))
        right_len = len(right)
        left_len = len(left)
        print(right, left, right_len, left_len, answer, types_len, right_len < types_len, left_len < types_len)
        if left_len < types_len and right_len < types_len:
            print(answer,"!!")
            result = answer
            return
        if right_len == types_len and start <= end:
            if end-start-1 < answer[1]-answer[0]:
                answer = [start+2, end]
            elif end-start-1 == answer[1]-answer[0] and start < answer[0]:
                answer = [start+2, end]
            two_pointer(start+1, end, answer)
        if left_len == types_len and start <= end:
            if end-start-1 < answer[1]-answer[0]:
                answer = [start+1, end-1]
            elif end-start-1 == answer[1]-answer[0] and start < answer[0]:
                answer = [start+1, end-1]
            two_pointer(start, end-1, answer)
    two_pointer(0, len(gems), [1, gems_len])
    return result