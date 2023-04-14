from itertools import permutations
import math

def is_prime_number(number):
    if number <= 1 : return False
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    prime_set = set()
    for i in range(1, len(numbers)+1):
        combi = list(map(''.join, list(set(list(permutations(numbers, i))))))
        for com in combi:
            if is_prime_number(int(com)) and int(com) not in prime_set:
                prime_set.add(int(com))
                answer += 1
    # combi = list(combinations(numbers))
    # print(combi)
    return answer