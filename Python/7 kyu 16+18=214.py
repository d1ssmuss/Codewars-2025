def add(num1, num2):
    if num1 > num2:
        num2 = str(num2).zfill(len(str(num1)))
    else:
        num1 = str(num1).zfill(len(str(num2)))
    nums1 = list(map(int, list(str(num1))))
    nums2 = list(map(int, list(str(num2))))
    numbers = [nums1[i] + nums2[i] for i in range(max(len(nums1), len(nums2)))]
    return int(''.join(map(str, numbers)))




print(add(72, 9))
print(add(16, 18))
print(add(122, 81))