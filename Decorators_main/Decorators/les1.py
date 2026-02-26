import os
from datetime import datetime
from functools import wraps


def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        args_str = ', '.join([repr(arg) for arg in args])
        # print(args_str) #  Проверка
        kwargs_str = ', '.join([f'{k}={repr(v)}' for k, v in kwargs.items()])
        # print(kwargs_str) #  Проверка

        all_args = []
        if args_str:
            all_args.append(args_str)
        if kwargs_str:
            all_args.append(kwargs_str)
        # print(all_args) #  Проверка
        arguments = ', '.join(all_args)
        # print(arguments) #  Проверка
        result = old_function(*args, **kwargs)

        log_entry = (
            f'{call_time} - '
            f'Function: {old_function.__name__} '
            f'called with arguments: ({arguments}) '
            f'returned: {repr(result)}\n'
        )
        with open('main.log', 'a', encoding='utf-8') as log_file:
            # print(log_entry) #  Проверка
            log_file.write(log_entry)

        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()