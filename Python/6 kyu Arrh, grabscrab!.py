def grabscrab(said, possible_words):
    answer = []
    for word in possible_words:
        if sorted(said) == sorted(word):
            answer.append(word)
    return answer if answer else []



print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))
print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]))
print('abcd' == 'bacd')