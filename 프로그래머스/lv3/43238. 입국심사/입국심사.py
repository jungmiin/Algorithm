def solution(n, times):
    answer = 0
    sorted_times = sorted(times)
    left = times[0]
    right = times[-1] * n
    
    while left <= right:
        mid = (left + right)//2
        available = 0
        for time in times:
            available += mid//time
            if available >= n:
                break
        if available >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
        
    return answer