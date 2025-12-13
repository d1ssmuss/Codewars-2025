def letters_to_numbers(s):
    total = 0
    for char in s:
        if char.isalpha():
            if char.isupper():
                total += 2 * (ord(char.lower()) - 96)
            else:
                total += ord(char) - 96
        elif char.isdigit():
            total += int(char)
        print(char, total)
    return total


print(letters_to_numbers("I Love You"))
print(letters_to_numbers("Give me five!"))