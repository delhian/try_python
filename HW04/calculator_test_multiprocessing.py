import requests
import os, time
from multiprocessing import Pool
import random

server_url = 'http://127.0.0.1:8080/'

number_of_executions = 1000
number_of_processes = 20

logfile_name = 'calculator_test_multiprocessing.log'



def get_data(c_type, first, second):
	url = server_url + c_type + '/' + first + '/' + second +'/'
	# print (url)
	return float(requests.get(url).content)


oper_dic = {'sum' : {'int_': [-27654321, 27654321], 'rep_': 5000}, 
			'min' : {'int_': [-27654321, 27654321], 'rep_': 3000},
			'mul' : {'int_': [-27654321, 27654321], 'rep_': 2000},
			'dev' : {'int_': [-27654321, 27654321], 'rep_': 2000},
			'pow' : {'int_': [1, 100], 'rep_': 200000}}



def generate_random_op(execution_id):
	proccess_id = os.getpid()
	fi = open('logfile_process'+ str(proccess_id), 'a')
	oper = random.choice(list(oper_dic.keys()))
	int_min = oper_dic[oper]['int_'][0]
	int_max = oper_dic[oper]['int_'][1]
	first = str(random.randint(int_min, int_max))
	second = str(random.randint(int_min, int_max))
	print ('current execution_id:',  execution_id, '...', first, oper, second, '=', get_data(oper, first, second), file=fi)
	fi.close()
	return (execution_id)

if __name__ == '__main__':
	f = open(logfile_name, 'w')
	print ('-----------------------', file=f)
	print ('multiprocessing test started', file=f)
	print ('-----------------------', file=f)

	print ('number_of_executions =', number_of_executions, 'number_of_processes =', number_of_processes, file=f)
	print ('multiprocessing test started')
	pool = Pool(processes = number_of_processes)
	pool.map(generate_random_op, range(number_of_executions))
	print ('multiprocessing test finished')

	print ('-----------------------', file=f)
	print ('multiprocessing test finished', file=f)
	print ('-----------------------', file=f)

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

# Многопоточность: 20 одновременных процессов. Через библиотеку multiprocessing
# Многопоточность: 20 одновременных процессов.