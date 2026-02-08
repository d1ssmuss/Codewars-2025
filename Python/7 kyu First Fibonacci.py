def solution(f, s):
    while True:
        prev_s = s - f
        prev_f = 2 * f - s
        if prev_s > f:
            return f,s
        elif prev_s < prev_f:
            return prev_s, f
        else:
            s = prev_s
            f = prev_f
        print(f,s)


# print(solution(398, 644))
# print(solution(15, 28)) # 2 and 13
# print(solution(186, 301)) # 3 and 7
print(solution(265, 429)) # 1 and 12
# print(solution(1186, 1919)) # 2 and 7
print(solution(814, 1317)) # 8 and 19
# print(solution(23, 36))