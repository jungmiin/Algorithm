def solution(storey):
    answer = 0
    while storey:
        value = storey%10
        if value > 5:
            answer += (10 - value)
            storey += (10 - value)
        elif value < 5:
            answer += value
            storey -= value
        else:
            if (storey//10)%10 > 4:
                answer += (10 - value)
                storey += (10 - value)
            else:
                answer += value
                storey -= value
        storey //= 10
        
    return answer