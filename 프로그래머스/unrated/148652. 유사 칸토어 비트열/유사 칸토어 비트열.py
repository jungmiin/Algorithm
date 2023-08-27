def solution(n, l, r):
    def cnt(n, m):
        if n == 1:
            return m if m < 3 else m-1
        span = 5**(n-1)
        prev = 4**(n-1)
        idx = m//span
        if idx < 2:
            return prev*idx + cnt(n-1, m-span*idx)
        elif idx == 2:
            return prev*idx
        elif idx > 2:
            return prev*(idx-1) + cnt(n-1, m-span*idx)
    return cnt(n, r) - cnt(n, l-1)