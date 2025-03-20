"""
Это первая часть этой серии ката. Вторая часть находится здесь, а третья часть - здесь

Добавьте два английских слова вместе!

Реализуйте класс Arith (struct struct Arith{значение : &'static str,} в Rust) таким образом, чтобы

//javascript
var k = new Arith("three");
k.add("seven"); //this should return "ten"

Входные данные - будут между нулем и десятью и всегда будут в нижнем регистре

Выходные данные - словесное представление результата сложения. Должно быть написано строчными буквами

"""

class Arith():
    def __init__(self, n1):
        self.n1 = n1


    def add(self, n2):
        self.n2 = n2
        numbers = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty"
        }
        word_numbers = {value: key for key, value in numbers.items()} # меняем местами ключ значение
        new_number = word_numbers[self.n1] + word_numbers[self.n2]
        return numbers[new_number]

