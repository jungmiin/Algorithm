import itertools

def solution(relation):

    c = len(relation[0])
    r = len(relation)
    combi = []
    
    for i in range(1, c+1):
        combi.extend(itertools.combinations(range(c), i))
        
    print(combi)
    
    answers = []
    
    for com in combi:
        li = [tuple(row[co] for co in com) for row in relation]
        if len(set(li)) == r:
            test = True
            # print(answers, com)
            for answer in answers:
                if set(answer).issubset(com):
                    test = False
                    break
            if test:
                answers.append(com)
    
    return len(answers)