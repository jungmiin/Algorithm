def solution(s):
    N = len(s)
    if len(s) == 1: return 1
    answer = 0
    # for i in range(1, N-1):
    #     if answer == N : return answer
    #     left, right = i-1, i+1
    #     while left >= 0 and right < N:
    #         if s[left] == s[right]:
    #             answer = max(answer, right-left+1)
    #             left -= 1
    #             right += 1
    #         else: break
    #     if s[i] == s[i+1]:
    #         left, right = i, i+1
    #         while left >= 0 and right < N:
    #             if s[left] == s[right]:
    #                 answer = max(answer, right-left+1)
    #                 left -= 1
    #                 right += 1
    #             else: break
    
    for i in range(len(s)):
        for j in range(1, N):
            n = j-i+1
            if answer == N: return answer
            if n < answer: continue
            if n%2 == 0: # 짝수
                if s[i:i+n//2] == s[j-N:i+n//2-N-1:-1]:
                    answer = max(answer, n)
            elif n%2 == 1: # 홀수
                if s[i:i+n//2] == s[j-N:i+n//2-N:-1]:
                    answer = max(answer, n)
    

    return answer