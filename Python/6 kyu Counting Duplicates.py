def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    arr = []
    ans = []
    for i in text:
        if i not in arr:
            arr.append(i)
        else:
            ans.append(i)
    return len(set(ans))
