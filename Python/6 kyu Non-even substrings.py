from itertools import combinations

def solve(s):
    # count = 0
    # arr = []
    # for k in range(1, len(s) + 1):
    #     for i in combinations(s, k):
    #         num = int(''.join(map(str, i)))
    #         if str(num) in s and num not in arr and num % 2 != 0:
    #             arr.append(num)
    #             count += s.count(str(num))
    # return count
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