import csv
import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

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

def format_phone(phone):
    if not phone:
        return ''
    phone_pattern = r'(\+7|8|7)?\s*[\(\s-]*(\d{3})[\)\s-]*\s*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})'
    ext_pattern = r'доб\s*(\d+)'
    main_match = re.search(phone_pattern, phone)
    if not main_match:
        return phone
    formatted = f"+7({main_match.group(2)}){main_match.group(3)}-{main_match.group(4)}-{main_match.group(5)}"
    ext_match = re.search(ext_pattern, phone, re.IGNORECASE)
    if ext_match:
        formatted += f" доб.{ext_match.group(2)}"
    return formatted

def fix_phones(contacts):
    fixed_contacts = [contacts[0]]
    for row in contacts[1:]:
        if len(row) > 5:
            phone = row[5]
            row[5] = format_phone(phone)
        fixed_contacts.append(row)
    return fixed_contacts

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

contacts_list = fix_fio(contacts_list)
contacts_list = fix_phones(contacts_list)
contacts_list = merge_duplicates(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook_new.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)