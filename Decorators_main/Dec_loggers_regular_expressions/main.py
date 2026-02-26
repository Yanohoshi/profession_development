import csv

from application.processing_fio import fix_fio, merge_duplicates
from application.processing_number_phone import fix_phones

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ

contacts_list = fix_fio(contacts_list)
contacts_list = fix_phones(contacts_list)
contacts_list = merge_duplicates(contacts_list)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook_new.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)