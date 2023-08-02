from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        if city.lower() not in cache:
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city.lower())
        else: 
            answer += 1
            if len(cache) >= cacheSize:
                cache.remove(city.lower())
            cache.append(city.lower())
            
    return answer