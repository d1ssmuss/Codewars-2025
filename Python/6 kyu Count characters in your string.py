def count(s):
    # The function code should be here
    return {letter:s.count(letter) for letter in set(s)}

while True:
    print(count(input()))