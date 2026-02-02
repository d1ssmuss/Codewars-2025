def is_square(arr):
    if arr:
        for i in arr:
            if (i ** 0.5).is_integer():
                continue
            else:
                return False
        else:
            return True
    else:
        return None

print(is_square([1,4,9,16, 17]))
print(is_square([1,4,9,16]))