def descending_order(num):
    return int(''.join(sorted(''.join(str(num)),reverse = True)))

print(descending_order(145263))