def persistence(n):
    count = 0
    if n <= 9:
        return 0
    else:
        res = 1
        num = n
        while (num >= 10):
            # print(num)
            for i in list(map(int, str(num))):
                res = res * i
            num = res
            res = 1
            count += 1
        return count




print(persistence(39))
# print(persistence(4))
# print(persistence(25))
# print(persistence(999))
