import time
import os

def loger_constructor_decor(file_name, file_path=None):  # Конструткор (нашел в интернете)
    if file_path is None:
        file_place = os.path.join(os.getcwd())
    else:
        file_place = os.path.join(os.path.abspath(file_path))

    file_path = os.path.join(file_place, file_name)

    def loger_decorator(old_function):  # Декоратор

        def new_func(*args, **kwargs):
            start = time.ctime(time.time())
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(f'Время запуска функции: {start}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args} и {kwargs}\n'
                           f'Результат: {result}\n'
                           f'|------------------------------->\n'
                           )
            return result

        return new_func

    return loger_decorator

def loger_decorator_my(old_function):  # Декоратор

    def new_func(*args, **kwargs):
        start = time.ctime(time.time())
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('decoratorlogs.txt', 'a', encoding='utf-8') as file:
            file.write(f'Время запуска функции: {start}\n'
                       f'Имя функции: {func_name}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n'
                       f'|------------------------------->\n'
                       )
        return result

    return new_func