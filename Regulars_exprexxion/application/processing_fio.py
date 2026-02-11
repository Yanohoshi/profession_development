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