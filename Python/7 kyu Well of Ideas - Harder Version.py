def well(arr):
    combined_list = []
    for i in range(len(arr)):
        combined_list += [str(arr[i][j]) for j in range(len(arr[i]))]
    # return list(map(str.lower, combined_list))
    if 1 <= list(map(str.lower, combined_list)).count("good") <= 2:
        return "Publish!"
    elif list(map(str.lower, combined_list)).count("good") > 2:
        return 'I smell a series!'
    else:
        return "Fail!"



print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]))
print(well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]))
print(well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]))

print(well([['bad', 3, 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]))