def chunk(lst, size):
# Принимает список - lst и целое число - size
# Возвращает список списков длиной в size, заполненных данными из списка lst
# Пример смотри ниже
	return_list = []
	sub_list = []
	for i, l in enumerate(lst):
		sub_list.append(l)
		if i % size == size - 1 or i == len(lst) - 1:
			return_list.append(sub_list)
			sub_list = []
	return return_list




def interpolate(string, data = {}):
# Это функция просто шаблонизирует данные из словаря data в строку string
# в таком же формате, как и метод .format строк.
# Т.е. заменяет все вхождения в строку string вида {ключ}
# на значение одноименного ключа в data
# Если такого ключа нет - то замены не происходит
	for i in data :
		string = string.replace('{'+i+'}', data[i])
	return string

print('chunk - test')
print(chunk(list(range(10)), 2))
print (chunk(list(range(10)), 3))
print (chunk(list(range(10)), 7))

print('interpolate - test')
print (interpolate('{a} {b}', {
'a': 'Hello',
'b': 'World'
}))
print(interpolate('{one} + {two} = 3', {
'one': '1',
'two': '2'
}))
print(interpolate('Nothing: {abc}', {'x': 'y'}))