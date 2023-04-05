def binary_number(number):
    tree_size = 0
    binary_number = format(number,'b')
    while tree_size < len(binary_number):
        tree_size = (tree_size + 1) * 2 - 1
    # print(str(binary_number).zfill(tree_size))
    return str(binary_number).zfill(tree_size)

def search(start, end, string):
    if start==end:
        return string[start]
    mid = (start + end) // 2
    # print("재귀", mid, string[mid], string[start:end+1])
    left = search(start, mid-1, string)
    if not left or (left == "1" and string[mid] == "0"): return False
    right = search(mid+1, end, string)
    if not right or (right == "1" and string[mid] == "0"): return False
    if left == "0" and right == "0" and string[mid] == "0": return "0"
    return "1"

def solution(numbers):
    answer = []
    for number in numbers:
        b_number = binary_number(number)
        result = search(0, len(b_number)-1, b_number)
        # print("끝", result)
        if result:
            answer.append(1)
        else:
            answer.append(0)
    return answer