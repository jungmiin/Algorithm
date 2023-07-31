from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(place, y, x):
    queue = deque()
    queue.append([y, x, 0]) # y좌표, x좌표, 시작점과의 맨하탄거리
    while queue:
        ty, tx, distance = queue.popleft()
        if distance > 1: break
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0<=nx<5 and 0<=ny<5:
                if (ny != y or nx != x) and place[ny][nx] == 'P':
                    return False
                elif place[ny][nx] == 'O':
                    queue.append([ny, nx, distance+1])
    return True

def solution(places):
    answer = []
    for place in places:
        people = []
        for row_index, row in enumerate(place):
            for column_index, column in enumerate(row):
                if column == 'P':
                    people.append([row_index, column_index])
        if len(people)==0:
            answer.append(1)
        else:
            is_obey = True
            for person in people:
                result = bfs(place, person[0], person[1])
                if not result: 
                    is_obey = False
                    break
            if is_obey :
                answer.append(1)
            else :
                answer.append(0)
                
            
    return answer