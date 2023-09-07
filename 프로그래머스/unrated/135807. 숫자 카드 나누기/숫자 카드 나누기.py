def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def solution(arrayA, arrayB):
    
    def find(li):
        n = 0
        for i in range(len(li)):
            n = gcd(n, li[i])
        return n
    
    def check(li, gcd):
        check = True
        for i in range(len(li)):
            if li[i]%gcd == 0:
                return False
        return True
    
    gcd_a, gcd_b = find(arrayA), find(arrayB)
    result_a, result_b = check(arrayB, gcd_a), check(arrayA, gcd_b)

    if result_a and result_b: return max(gcd_a, gcd_b)
    elif result_a : return gcd_a
    elif result_b : return gcd_b
    else : return 0