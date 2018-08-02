import requests
import time
import random

server_url = 'http://127.0.0.1:8080/'
logfile_name = 'calculator_test.log'

def get_data(c_type, first, second):
	url = server_url + c_type + '/' + first + '/' + second +'/'
	print (url)
	return float(requests.get(url).content)


oper_dic = {'sum' : {'int_': [-27654321, 27654321], 'rep_': 5000}, 
            'min' : {'int_': [-27654321, 27654321], 'rep_': 3000},
            'mul' : {'int_': [-27654321, 27654321], 'rep_': 2000},
            'dev' : {'int_': [-27654321, 27654321], 'rep_': 2000},
            'pow' : {'int_': [1, 100], 'rep_': 2000}}

# тестирование 

print ('operations test started')
f = open(logfile_name, 'w')
print ('-----------------------', file=f)
print ('operations test started', file=f)
print ('-----------------------', file=f)


for oper in oper_dic:
	starttime=time.time()
	n_of_op = oper_dic[oper]['rep_']
	for i in range(oper_dic[oper]['rep_']):
		int_min = oper_dic[oper]['int_'][0]
		int_max = oper_dic[oper]['int_'][1]
		first = str(random.randint(int_min, int_max))
		second = str(random.randint(int_min, int_max))
	duration = time.time() - starttime
	print ('Operation', oper,':', n_of_op, ' repetitions per', duration, 'sec', file=f)

print ('-----------------------', file=f)
print ('operations test finished', file=f)
print ('-----------------------', file=f)
print ('operations test finished')
f.close()
print (logfile_name, 'created')

# Учимся писать программу и тестировать её же.

# Есть веб-сервер. На нем работает калькулятор. На flask. Погуглить и почитать что это такое.
# server.py.zip

# Написать тесты для калькулятора.
# API сервера
# http://127.0.0.1:8080/функция/int/int/

# Возврат:
# 200 - верный запрос и ответ с вычислениями.
# 404 - неверная страница

# Функции:
# sum - сложение
# min - вычитание
# mul - умножение
# dev - деление
# pow - возведение в степень

# int:
# Целые числа от -27654321 до 27654321.

# Требования
# sum - сложение | 5000 запросов в минуту
# min - вычитание | 3000 запросов в минуту
# mul - умножение | 2000 запросов в минуту
# dev - деление | 2000 запросов в минуту
# pow - возведение в степень | 2000 запросов в минуту
