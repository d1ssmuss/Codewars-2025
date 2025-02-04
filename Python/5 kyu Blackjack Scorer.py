import unittest
def score_hand(cards):
    """
    Выполните функцию, которая определяет счет раздачи в карточной игре Блэкджек (она же 21 очко).

    Функция получает массив строк, представляющих каждую карту в раздаче (("2", "3", ..., "10", "J", "Q", "K" или "A"),
    и должна возвращать результат раздачи (целое число).

    Правила подсчета очков:
    Карты с номерами считаются по номиналу (от 2 до 10). Валет, дама и король считаются за 10.
    Туз может быть засчитан как 1 или 11.

    Верните самый высокий балл из карт, который меньше или равен 21.
    Если нет очков меньше или равных 21, верните наименьший балл, который больше 21.

    Примеры
    ["A"] ==> 11
    ["A", "J"] ==> 21
    ["A", "10", "A"] ==> 12
    ["5", "3", "7"] ==> 15
    ["5", "4", "3", "2", "A", "K"] ==> 25
    :param cards:
    :return:
    """
    # score = 0
    highest_score = 0
    for i in cards:
        if i in "KJQ":
            highest_score += 10
        elif i == "A":
            highest_score += 11
        else:
            highest_score += int(i)
    count_Ace = cards.count("A")
    while highest_score > 21 and count_Ace:
        highest_score -= 10
        count_Ace -= 1
    return highest_score


print(score_hand(['2', '3']), 5)
print(score_hand(['4', '5', '6']), 15)
print(score_hand(['7', '7', '8']), 22)
print(score_hand(['9', '2', '10']), 21)
print(score_hand(['4', '7', '8']), 19)
print("------------------------------")
# Score J, Q and K as 10
print(score_hand(['J', '3']), 13)
print(score_hand(['J', 'Q']), 20)
print(score_hand(['K', 'J', 'Q']), 30)
print("------------------------------")
# Score hands with Aces correctly
print(score_hand(['A', '3']), 14)
print(score_hand(['A', 'J']), 21)
print(score_hand(['A', 'A', 'A', 'J']), 13)
print(score_hand(['A', '2', 'A', '9', '9']), 22)
print("------------------------------")
# some tricky aces
print(score_hand(['A', 'A']), 12)
print(score_hand(['8', 'A', 'A']), 20)
print(score_hand(['5', '4', 'A', 'A']), 21)
print(score_hand(['A', '2', 'A', '3', 'A']), 18)
print(score_hand(['A', 'A', 'A', 'A']), 14)


