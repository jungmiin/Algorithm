from itertools import combinations
from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    N = len(begin)
    cases = list(combinations(range(N), N-1))
    adj = {word:[] for word in words}
    adj[begin] = []
    
    for word in words:
        for key, value in adj.items():
            if key == word: continue
            elif key[1:] == word[1:] or key[:-1] == word[:-1]: adj[key].append(word)
            else:
                for case in cases:
                    possible = True
                    for i in case:
                        if key[i] != word[i]:
                            possible = False
                    if possible: 
                        adj[key].append(word)
                        continue
                        
    def bfs():
        q = deque()
        visited = []
        q.append((begin, 0))
        visited.append(begin)
        while q:
            word, cost = q.popleft()
            if word == target:
                return cost
            for nword in adj[word]:
                if nword not in visited:
                    q.append((nword, cost+1))
                    visited.append(nword)
    return bfs()