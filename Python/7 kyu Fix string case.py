def solve(s):
    up, down = 0, 0
    for i in s:
        if i.isupper():
            up += 1
        else:
            down += 1
    if up > down:
        return s.upper()
    else:
        return s.lower()


print(solve("code"))
print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))