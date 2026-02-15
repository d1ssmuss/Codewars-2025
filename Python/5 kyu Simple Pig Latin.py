def pig_it(text):
    answer = []
    for word in text.split():
        if word.isalpha():
            word = word[1:] + word[0] + 'ay'
        answer.append(word)
    return ' '.join(answer)



print(pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
print(pig_it('This is my string') == 'hisTay siay ymay tringsay')
