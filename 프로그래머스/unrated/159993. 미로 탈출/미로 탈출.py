from collections import deque

def solution(maps):
    answer = 0
    row, col = len(maps), len(maps[0])
    start, lever, exit = [], [], []
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
            elif maps[i][j] == 'E':
                exit = [i, j]
    
    def bfs(sr, sc, tr, tc):
        visited = [list([-1] * col) for _ in range(row)]
        queue = deque()
        queue.append((sr, sc))
        visited[sr][sc] = 0
        answer = -1
        while queue:
            r, c = queue.popleft()
            if r == tr and c == tc:
                return visited[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0<=nr<row and 0<=nc<col and visited[nr][nc] == -1 and maps[nr][nc] != 'X':
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c]+1
        return answer
    
    distance_1 = bfs(start[0], start[1], lever[0], lever[1])
    distance_2 = bfs(lever[0], lever[1], exit[0], exit[1])
    if distance_1 == -1 or distance_2 == -1:
        return -1
    else:
        return distance_1 + distance_2
