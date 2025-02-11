def nth_char(words):
	"""
	Выполните функцию, которая принимает массив слов.

	Вы должны объединить n-ю букву из каждого слова, чтобы создать новое слово, которое должно быть возвращено в виде строки, где n - позиция слова в списке.

	Например:
	["yoda", "best", "has"]  -->  "yes"
	  ^        ^        ^
	  n=0     n=1     n=2

	Примечание:
	Тестовые примеры содержат только допустимые входные данные
	т.е. массив строк или пустой массив;
	и в каждом слове должно быть достаточно букв.
	:param words:
	:return:
	"""
	return "".join([words[i][i] for i in range(len(words))])


print(nth_char(['yoda', 'best', 'has']))
print(nth_char([]))
print(nth_char(['X-ray']))
print(nth_char(['No', 'No']))
print(nth_char(['Chad','Morocco','India','Algeria','Botswana','Bahamas','Ecuador','Micronesia']))