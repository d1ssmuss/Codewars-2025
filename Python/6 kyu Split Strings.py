def solution(s):
    arr = []
    for i in range(len(s)):
        if i % 2 == 0:
            v = s[i:i+2]
            # print(v)
            if len(v) != 2:
                v += "_"
            arr.append(v)
    return arr


print(solution('abcdef'))