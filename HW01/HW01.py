def capitalize(string):
# Принимает строку и заменяет первую букву каждого слова на заглавную.
# Слова отделяются друг от друга пробелами и переходом строки
# 'this is my world' -> 'This Is My World'
# 'hello' -> 'Hello'
# 'one
# two' ->
# 'One
# Two'
	split_substr = [' ', '\n' ]
	new_string = ''
	if_capitalize = True
	for st in string:
		if if_capitalize:
			st = st.capitalize()
			if_capitalize = False
		if st in split_substr:
			if_capitalize = True
		new_string += st
	return new_string


def parenthesis(string):
# Принимает строку, которая может содержать скобки.
# Возвращает кортеж из двух элементов, где:
# 1-й элемент - это исходная строка, но первое корректное вхождение выражения
# внутри скобок заменено на символ $
# 2-й элемент - это то, что находилось в этих скобках
# paretntesize('1 + (3 + 8)') # возвращает ('1 + $', '3 + 8')
# paretntesize('1 + 3') # возвращает ('1 + 3', None)
# paretntesize('(b + c)') # возвращает ('$', 'b + c')
	start_  = string.find('(')
	end_  = string.find(')')
	if start_parenthesis == -1:
		return (string, None)
	else:
		str1 = string[0:start_]+'$'+string[end_+1:]
		str2 = string[start_+1:end_]
		return (str1, str2)

print('capitalize - test')
print(capitalize ('this is my world'))
print(capitalize ('hello'))
print(capitalize ('one\ntwo'))

print('parenthesis - test')
print(parenthesis('1 + (3 + 8)'))
print(parenthesis('1 + 3'))
print(parenthesis('(b + c)'))



