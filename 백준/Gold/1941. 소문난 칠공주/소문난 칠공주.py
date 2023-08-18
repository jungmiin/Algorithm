import sys
from collections import deque

input = sys.stdin.readline

graph = [ list(input().rstrip()) for _ in range(5) ]

queue = []
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
answer = 0

def is_connected(queue):
    r, c = queue[0]
    visited = [ [False]*5 for _ in range(5) ]
    for r, c in queue:
        visited[r][c] = True
    q = deque()
    q.append((r, c))
    visited[r][c] = False
    check = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc]:
                visited[nr][nc] = False
                check += 1
                q.append((nr, nc))
    if check == 7: return True
    else: return False
        
def dfs(length, start, y_count):
    global answer
    if y_count >= 4:
        return
    if length == 7:
        if is_connected(queue):
            answer += 1
            return
    for i in range(start, 25):
        queue.append((i//5, i%5))
        dfs(length+1, i+1, y_count + int(graph[i//5][i%5] == "Y"))
        queue.pop()

dfs(0, 0, 0)

print(answer)