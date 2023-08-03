def delete(coords, board):
    score = 0
    for [i, j] in coords:
        if board[i][j] != '~':
            score += 1
            list_board = list(board[i])
            list_board[j] = '~'
            board[i] = ''.join(list_board)
        if board[i+1][j] != '~':
            score += 1
            list_board = list(board[i+1])
            list_board[j] = '~'
            board[i+1] = ''.join(list_board)
        if board[i][j+1] != '~':
            score += 1
            list_board = list(board[i])
            list_board[j+1] = '~'
            board[i] = ''.join(list_board)
        if board[i+1][j+1] != '~':
            score += 1
            list_board = list(board[i+1])
            list_board[j+1] = '~'
            board[i+1] = ''.join(list_board)
    return [board, score]

def drop(board):
    for i in range(len(board)-2, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != '~' and board[i+1][j] == '~':
                for k in range(len(board)-1, i, -1):
                    if board[k][j] == '~':
                        list_board = list(board[i])
                        list_board_drop = list(board[k])
                        list_board_drop[j] = list_board[j]
                        list_board[j] = '~'
                        board[i] = ''.join(list_board)
                        board[k] = ''.join(list_board_drop)
    return board

def solution(m, n, board):
    answer = 0
    
    while True:
        tmp = 0
        coords = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '~' and board[i+1][j] == board[i][j] and board[i][j+1] == board[i][j] and board[i+1][j+1] == board[i][j]:
                    tmp += 4
                    coords.append([i, j])
        # print(coords)
        if not coords:
            break;
        else:
            [board, score] = delete(coords, board)
            answer += score
            board = drop(board)
    print(board)
    return answer