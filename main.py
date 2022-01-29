from dec import loger_constructor_decor, loger_decorator_my
from logs import result_file_name as re, result_dir as re_dir

nested_list_1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

@loger_constructor_decor(re, re_dir)
def division(a, b):
    return a * b

@loger_decorator_my
def flat_generator(nested_list_1):
	"""Задание 2 генератор"""
	for item in nested_list_1:
		for i in item:
			yield i

if __name__ == '__main__':
    division(1000, 7888)
    division(1111111, 5)
    division(22, 1)

    flat_generator(nested_list_1)