dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

INF = 1e9

def can_lose(board, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
            return False
    return True

def dfs(board, r1, c1, r2, c2):
    
    if can_lose(board, r1, c1):
        return [False, 0]
    
    if r1 == r2 and c1 == c2:
        return [True, 1]
    
    min_turn = INF
    max_turn = 0
    can_win = False
    
    for i in range(4):
        nr = r1 + dr[i]
        nc = c1 + dc[i]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc]:
            board[r1][c1] = 0
            result = dfs(board, r2, c2, nr, nc)
            board[r2][c2] = 1
            if not result[0]:
                can_win = True
                min_turn = min(min_turn, result[1])
            elif not can_win:
                max_turn = max(max_turn, result[1])
    turn = min_turn if can_win else max_turn
    return [can_win, turn + 1]
                
            
        

def solution(board, aloc, bloc):    
    is_win, answer = dfs(board, aloc[0], aloc[1], bloc[0], bloc[1])
    print(is_win, answer)
    return answer