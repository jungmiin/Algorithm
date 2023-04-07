from collections import deque

#lrud
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
ds = ["d", "l", "r", "u"]

def bfs(n, m, x, y, r, c, k, answer):
    queue = deque()
    queue.append((x,y,""))
    while queue:
        tx, ty, string = queue.popleft()
        if (x,y) == (r,c) and (k - len(string) ) % 2 == 1:
            return
        if len(string) == k:
            if tx == r and ty == c:
                answer = min(answer, string)
            continue
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx <= 0 or nx > n or ny <= 0 or ny > m: continue
            if abs(nx - r) + abs(ny - c) + len(string) + 1 > k:continue
            nstring = string+ds[i]
            queue.append((nx, ny, nstring))
            break
    return answer

def solution(n, m, x, y, r, c, k):
    answer = "z"
    answer = bfs(n, m, x, y, r, c, k, answer)
    if answer != "z": return answer
    else : return "impossible"