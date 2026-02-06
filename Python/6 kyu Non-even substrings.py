from itertools import combinations

def solve(s):
    a = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if int(s[i:j]) % 2 != 0:
                a.append(s[i:j])
                print(i,j, s[i:j])
    return len(a)

print(solve("1341"))

print(solve("626191763941342778489957855271571237491936466781236758494959923925797188679833145725"))
