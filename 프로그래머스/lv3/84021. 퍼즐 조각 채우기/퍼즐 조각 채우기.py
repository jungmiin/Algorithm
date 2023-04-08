import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(N, graph, x, y, position):
    queue = [position]
    graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph) and graph[nx][ny] == N:
            queue += dfs(N, graph, nx, ny, (position[0] + dx[i], position[1] + dy[i]))
    return queue

def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = table[i][j]

    return rotated

def solution(game_board, table):
    
    answer = 0
    slots = []
    
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                slots.append(dfs(0, game_board, i, j, (0, 0)))
    
    for _ in range(4):
        table = rotate(table)
        copy_table = copy.deepcopy(table)
        for i in range(len(copy_table)):
            for j in range(len(copy_table)):
                if copy_table[i][j] == 1:
                    piece = dfs(1, copy_table, i, j, (0, 0))
                    print(piece)
                    if piece in slots:
                        slots.remove(piece)
                        answer += len(piece)
                        table = copy.deepcopy(copy_table)
                    else: 
                        copy_table = copy.deepcopy(table)
                        
    return answer