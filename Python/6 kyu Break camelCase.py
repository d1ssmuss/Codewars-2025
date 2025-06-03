def solution(s):
    for i in range(65, 91):
        letter = chr(i)
        s = s.replace(letter, " " + letter)
    return s


print(solution("breakCamelCase"))