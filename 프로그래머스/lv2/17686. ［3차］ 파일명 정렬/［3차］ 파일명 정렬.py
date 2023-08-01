def solution(files):
    answer = []
    split_files = [[""]*3 for _ in range(len(files))] # HEAD, NUMBER, TAIL

    for file_index, file in enumerate(files):
        cur = 0 # 0-HEAD, 1-NUMBER, 2-TAIL
        for char_index, char in enumerate(file):
            if cur == 0:
                split_files[file_index][cur] += char
                if file[char_index+1].isdigit():
                    cur += 1
            elif cur == 1:
                split_files[file_index][cur] += char
                if len(file) > char_index+1 and not file[char_index+1].isdigit():
                    cur += 1
            else:
                split_files[file_index][cur] = file[char_index:]
                break
    sorted_files = sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))
    # print(sorted_files)
    return [''.join(file) for file in sorted_files]