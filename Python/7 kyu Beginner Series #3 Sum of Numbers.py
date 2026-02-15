def get_sum(a,b):
    if a == b:
        return a
    else:
        if a > b:
            b, a = a, b
        print(*range(a, b + 1))
        return sum(range(a, b + 1))


print(get_sum(20, 12))