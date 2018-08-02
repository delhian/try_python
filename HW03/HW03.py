def parse(str):
# Исполнить функцию, которая разбирает строку во вложенную структуру.
# Вызов: parse('1 + 2 - 3 * 4')
# возврат: ['+', '1', ['-', '2', ['*', '3', '4']]]
	signs = ['+', '-', '*', '/']
	ret = []
	# преобразуем в список по разделителю пробел:
	str_list = str.split(' ') 
	for ind, i in enumerate(str_list):
		if i in signs:
			ret.insert(0, i)
			# оставшаяся часть списка:
			str_list_rest = str_list[ind + 1:]
			# проверяем, что это - последний элемент в списке
			if len(str_list_rest) == 1:
				ret.append(str_list_rest[0])
			else:
				ret.append(parse(' '.join(str_list_rest)))
			return ret
		else:
			ret.append(i)

print('parse - test')
print(parse('1 + 2 - 3 * 4'))

print(parse('1 * 2 / 33 * 4 - 7 + 89 / 8 * 6'))