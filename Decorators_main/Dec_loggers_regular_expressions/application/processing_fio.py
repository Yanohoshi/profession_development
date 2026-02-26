from datetime import datetime


def fix_fio(contacts):
    fixed_contacts = [contacts[0]]
    for row in contacts[1:]:
        fio = ' '.join(row[:3])
        fio_parts = fio.split()
        while len(fio_parts) < 3:
            fio_parts.append('')
        new_row = fio_parts[:3] + row[3:]
        fixed_contacts.append(new_row)
    return fixed_contacts


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            # Получаем текущую дату и время
            call_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Формируем строку с аргументами
            args_str = ', '.join([repr(arg) for arg in args])
            kwargs_str = ', '.join([f'{k}={repr(v)}' for k, v in kwargs.items()])

            # Объединяем позиционные и именованные аргументы
            all_args = []
            if args_str:
                all_args.append(args_str)
            if kwargs_str:
                all_args.append(kwargs_str)

            arguments = ', '.join(all_args)

            # Вызываем исходную функцию и получаем результат
            result = old_function(*args, **kwargs)

            # Формируем строку для записи в лог
            log_entry = (
                f'{call_time} - '
                f'Function: {old_function.__name__} '
                f'called with arguments: ({arguments}) '
                f'returned: {repr(result)}\n'
            )

            # Записываем в указанный файл
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_entry)

            return result

        return new_function

    return __logger

@logger('merge_duplicates.log')
def merge_duplicates(contacts):
    merged_dict = {}

    for row in contacts[1:]:
        lastname = row[0]
        firstname = row[1]
        key = (lastname.strip().lower(), firstname.strip().lower())

        if key in merged_dict:
            existing = merged_dict[key]
            for i in range(len(row)):
                if row[i] and not existing[i]:
                    existing[i] = row[i]
        else:
            merged_dict[key] = row.copy()
    result = [contacts[0]]
    result.extend(merged_dict.values())
    return result