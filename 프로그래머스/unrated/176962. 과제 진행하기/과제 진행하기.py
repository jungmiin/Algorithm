from heapq import heappush, heappop

def solution(input_plans):
    plans = []
    pause = []
    answer = []
    def do_pause(start, next_start):
        if not pause:
            return
        _, playtime, name = heappop(pause)
        if start + playtime <= next_start:
            answer.append(name)
            do_pause(start + playtime, next_start)
        else:
            heappush(pause, (_, playtime - (next_start-start), name))
            return
        
    for name, start, playtime in input_plans:
        hour, minute = map(int, start.split(':'))
        start = hour*60 + minute
        heappush(plans, (start, int(playtime), name))
    while len(plans) >= 2:
        start, playtime, name = heappop(plans)
        next_start, next_playtime, next_name = heappop(plans)
        if start + playtime <= next_start:
            answer.append(name)
            if start + playtime < next_start and pause:
                do_pause(start + playtime, next_start)
        else:
            heappush(pause, (-start, playtime-(next_start-start), name))
        heappush(plans, (next_start, next_playtime, next_name))
    start, playtime, name = heappop(plans)
    answer.append(name)
    while pause:
        start, playtime, name = heappop(pause)
        answer.append(name)
    return answer
# def solution(plans):
#     answer = []
#     pause = []
#     plans = sorted(plans, key=lambda x: x[1])
#     def do_pause (start, next_start):
#         if not pause:
#             return
#         name, playtime = pause.pop()
#         if start + playtime <= next_start:
#             answer.append(name)
#             do_pause(start+playtime, next_start)
#         else: 
#             pause.append([name, playtime])
#             return
    
#     for i in range(len(plans)):
#         # print(answer, pause)
#         name, start, playtime = plans[i]
#         hour, minute = map(int, start.split(':'))
#         start = hour*60 + minute
#         if i+1 < len(plans):
#             n_hour, n_minute = map(int, plans[i+1][1].split(':'))
#             n_start = n_hour*60 + n_minute
#             if start + int(playtime) <= n_start:
#                 answer.append(name) 
#                 if start + int(playtime) < n_start:
#                     do_pause(start + int(playtime), n_start)
#             else:
#                 pause.append([name, int(playtime) - (n_start - start)])
#         else: answer.append(name)
#     while pause:
#         name, _ = pause.pop()
#         answer.append(name)
#     return answer