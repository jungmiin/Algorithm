from heapq import heappush, heappop
def solution(n, cores):
    # 작업 n개를 하는데 걸리는 시간 = start, end
    # 작업 개수 = target
    start = 0
    end = max(cores) * n
    N = len(cores)
    
    while start < end:
        mid = (start+end)//2
        work = N
        for core in cores:
            work += mid // core
        if work >= n:
            end = mid
        else:
            start = mid+1
        
    work = N
    for core in cores:
        work += (end-1) // core
    remain_work = n - work

    for i, core in enumerate(cores):
        if end % core == 0:
            remain_work -= 1
            if remain_work == 0:
                return i + 1