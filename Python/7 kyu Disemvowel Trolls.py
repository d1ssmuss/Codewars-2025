def disemvowel(string_):
    return ''.join([i for i in string_ if i.lower() not in 'aieou'])


print(disemvowel("This website is for losers LOL!"))
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))