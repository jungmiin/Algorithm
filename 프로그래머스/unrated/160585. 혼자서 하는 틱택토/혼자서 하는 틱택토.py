# O가 이미 이겼는데 -> X가 O의 갯수와 같거나 큼
# X가 이미 이겼는데 -> O가 X보다 큼
# O의 갯수보다 X의 갯수가 큼
# O의 갯수와 X의 갯수가 2이상 차이남

def o_win(board):
    for i in range(3):
        if board[i] == "OOO":
            return True
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return True
    if board[0][0] == board[1][1] == board[2][2] == "O" or board[2][0] == board[1][1] == board[0][2] == "O":
        return True
    return False
def x_win(board):
    for i in range(3):
        if board[i] == "XXX":
            return True
        elif board[0][i] == board[1][i] == board[2][i] == "X":
            return True
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[2][0] == board[1][1] == board[0][2] == "X":
        return True
    return False

def solution(board):
    answer = -1
    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O": o_cnt += 1
            if board[i][j] == "X": x_cnt += 1
    if o_cnt-x_cnt > 1:
        return 0
    if x_cnt > o_cnt:
        return 0
    if o_win(board) and x_cnt >= o_cnt:
        return 0
    if x_win(board) and o_cnt > x_cnt:
        return 0
    return 1