from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N = 102

def bfs(plane, cx, cy, ix, iy):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((cy, cx))
    visited[cy][cx] = 0
    while queue:
        y, x,  = queue.popleft()
        if iy == y and ix == x:
            return visited[y][x] // 2
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if plane[ny][nx] == 1 and visited[ny][nx] == -1:
                queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    plane = [ [-1]*N for _ in range(N) ]
    for rect in rectangle:
        lx, ly, rx, ry = map(lambda x: x*2, rect)
        for i in range(ly, ry+1):
            for j in range(lx, rx+1):
                if ly < i < ry and lx < j < rx:
                    plane[i][j] = 0
                elif plane[i][j] != 0:
                    plane[i][j] = 1
    return bfs(plane, characterX*2, characterY*2, itemX*2, itemY*2)