from collections import defaultdict
def solution(survey, choices):
    answer = ''
    init = ["RT", "CF", "JM", "AN"]
    types = defaultdict(int)
    for i in range(len(choices)):
        if 0 < choices[i] < 4:
            types[survey[i][0]] += 4-choices[i]
        elif 4 < choices[i] < 8:
            types[survey[i][1]] += choices[i]-4
    for i in init:
        if types[i[0]] < types[i[1]]:
            answer += i[1]
        else:
            answer += i[0]
    return answer