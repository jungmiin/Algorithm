def solution(citations):
    answer = 0
    counts = sorted(range(max(citations)+1), key=lambda x: -x)
    for count in counts:
        print(count)
        up = 0
        down = 0
        for citation in citations:
            if citation >= count: up += 1
            else : down += 1
        if up >= count and down <= count:
            return count
    return answer