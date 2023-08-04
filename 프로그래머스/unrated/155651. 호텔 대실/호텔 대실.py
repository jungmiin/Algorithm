from heapq import heappop, heappush

def solution(book_time):
    times = [[int(start[:2])*60+int(start[3:]),int(end[:2])*60+int(end[3:])] for start, end in book_time]
    times.sort()
    room = 1  
    hq = []
    for start, end in times:
        if not hq:
            heappush(hq, end)
            continue
        if hq[0]+10 <= start:
            heappop(hq)
        else:
            room += 1
        heappush(hq, end)
    return room