def solve(arr):
    stack = []
    for i in arr:
        if i not in stack:
            stack.append(i)
        else:
            stack.remove(i)
            stack.append(i)
    return stack

print(solve([3,4,4,3,6,3]))
print((solve([1,2,1,2,1,2,3])))
print(solve([1,2,3,4]))
print(solve([1,1,4,5,1,2,1]))