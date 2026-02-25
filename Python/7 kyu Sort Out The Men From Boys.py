def men_from_boys(arr):
    arr = sorted(arr)
    even = []
    odd = []
    for i in arr:
        if i not in even and i not in odd:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
    return even + odd[::-1]

print(men_from_boys([72, 76, 76, 82, 100, 91, 85]))