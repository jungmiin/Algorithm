import math

# 소수 구하기
def get_primes(number):
    primes = [True for _ in range(number+1)]
    for i in range(2, int(math.sqrt(number))+1):
        if primes[i]:
            j = 2
            while i*j <= number:
                primes[i*j] = False
                j+=1
    res = []
    for i in range(2, number+1):
        if primes[i]:
            res.append(i)
    return res

# 준소수 구하기
def get_subprimes(number, primes):
    subprimes = set()
    for prime1 in primes:
        for prime2 in primes:
            if prime1 * prime2 > number:
                break
            subprimes.add(prime1 * prime2)
    return list(sorted(subprimes))


def solution(N, P, Q):
    primes = get_primes(N//2)
    subprimes = get_subprimes(N, primes)

    # 누적합
    sums = [0 for _ in range(N+1)]
    for subprime in subprimes:
        sums[subprime] += 1
    for i in range(1, N+1):
        sums[i] += sums[i-1]
        
    answers = []
    for i in range(len(P)):
        answers.append(sums[Q[i]]-sums[P[i]-1])
        
    return answers