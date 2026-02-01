def small_enough(array, limit):
    return True if len([i for i in array if i <= limit]) == len(array) else False
