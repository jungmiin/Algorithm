from copy import deepcopy
import sys
input = sys.stdin.readline

TEST_CASE = 1 # 테스트 케이스 수

answer = 11
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def solution():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    def tilt(board, d, b, r):
        br, bc = b
        rr, rc = r
        nbr, nbc, nrr, nrc = br+dr[d], bc+dc[d], rr+dr[d], rc+dc[d]
        b_drop, r_drop = False, False
        for _ in range(10):
            b_drop, r_drop = False, False
            if 0<=nrr<N and 0<=nrc<M:
                if board[nrr][nrc] == 'O':
                    r_drop = True
                    board[rr][rc] = '.'
                elif board[nrr][nrc] == '.':
                    board[nrr][nrc] = board[rr][rc]
                    board[rr][rc] = '.'
                    rr, rc = nrr, nrc
            if 0<=nbr<N and 0<=nbc<M:
                if board[nbr][nbc] == 'O':
                    b_drop = True
                    board[br][bc] = '.'
                elif board[nbr][nbc] == '.':
                    board[nbr][nbc] = board[br][bc]
                    board[br][bc] = '.'
                    br, bc = nbr, nbc
            nbr, nbc, nrr, nrc = br+dr[d], bc+dc[d], rr+dr[d], rc+dc[d]
        if b_drop: 
            return ('b', board, (br, bc), (rr, rc))
        if not b_drop and r_drop:
            return ('r', board, (br, bc), (rr, rc))
        else:
            return ('', board, (br, bc), (rr, rc))
    def dfs(board, cnt, b, r):
        global answer
        if cnt>10:
            return
        for i in range(4):
            drop, nboard, nb, nr = tilt(deepcopy(board), i, b, r)
            if drop == 'r':
                answer = min(answer, cnt)
                if answer == 1:
                    return
            elif drop == '':
                if nb != b or nr != r:
                    dfs(nboard, cnt+1, nb, nr)
    br, bc, rr, rc = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'B':
                br, bc = i, j
            if board[i][j] == 'R':
                rr, rc = i , j
    dfs(board, 1, (br, bc), (rr, rc))
    print(-1) if answer == 11 else print(answer)

for _ in range(TEST_CASE):
    answer = 11
    solution()