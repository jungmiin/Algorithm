answer = 0

def condition(queens, nr, nc):
    for r in range(nr):
        if queens[r] == nc or (abs(nr-r) == abs(nc-queens[r])):
            return False
    return True

def dfs(n, r, queens):
    # print(r, queens)
    if r == n:
        return 1
    cnt = 0
    for c in range(n):
        if condition(queens, r, c):
            queens[r] = c
            cnt += dfs(n, r+1, queens)
    return cnt

def solution(n):
    queens = [-1]*n
    return dfs(n, 0, queens)