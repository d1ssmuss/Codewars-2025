def distinct(seq):
    stack = []
    for i in seq:
        if i not in stack:
            stack.append(i)
    return stack
