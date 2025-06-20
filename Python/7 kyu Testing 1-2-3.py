def number(lines):
    return [f"{i+1}: {lines[i]}" for i in range(len(lines))]


a = number(["a", "b", "c"])
print(a)