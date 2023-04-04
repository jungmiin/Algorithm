def solution(board, skills):
    row_length = len(board)
    column_length = len(board[0])
    tmp = [[0] * (column_length+1) for _ in range(row_length+1)]
    answer = 0
    
    for type, r1, c1, r2, c2, degree in skills:
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2+1] += -degree if type == 2 else degree
        tmp[r2+1][c1] += -degree if type == 2 else degree
        tmp[r2+1][c2+1] += degree if type == 2 else -degree
    
    for i in range(row_length):
        for j in range(column_length):
            tmp[i][j+1] += tmp[i][j]
            
    for i in range(column_length):
        for j in range(row_length):
            tmp[j+1][i] += tmp[j][i]
    
    for i in range(row_length):
        for j in range(column_length):
            board[i][j] += tmp[i][j]
            if board[i][j] > 0:
                answer += 1
        
    return answer