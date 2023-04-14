def make_yellow_list(yellow):
    yellow_list = []
    for i in range(1, yellow+1):
        if yellow%i == 0:
            yellow_list.append((i, yellow/i))
    return yellow_list

def solution(brown, yellow):
    answer = []
    yellow_list = make_yellow_list(yellow)
    for h, v in yellow_list:
        if 2*(h+2) + v*2 == brown:
            return [v+2, h+2]