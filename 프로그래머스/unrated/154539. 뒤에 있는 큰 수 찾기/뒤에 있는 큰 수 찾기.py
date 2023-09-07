def solution(numbers):
    dp = [-1] * len(numbers)
    max_number = max(numbers)
    
    for i in range(len(numbers)-2, -1, -1):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                dp[i] = numbers[j]
                break
            else:
                if dp[j] == -1:
                    dp[i] = -1
                    break
                elif numbers[i] < dp[j]:
                    dp[i] = dp[j]
                    break
            # elif numbers[i] == max_number:
            #     dp[i] = -1
            #     break
    
    return dp