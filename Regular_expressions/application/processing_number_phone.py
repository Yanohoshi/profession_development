import re


def format_phone(contacts):
    def format_single(phone):
        if not phone:
            return ''

        phone_pattern = r'(\+7|8|7)?\s*[\(\s-]*(\d{3})[\)\s-]*\s*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})'
        ext_pattern = r'доб\.?\s*(\d+)'

        main_match = re.search(phone_pattern, str(phone))
        if not main_match:
            return phone
        formatted = f"+7({main_match.group(2)}){main_match.group(3)}-{main_match.group(4)}-{main_match.group(5)}"
        ext_match = re.search(ext_pattern, str(phone), re.IGNORECASE)
        if ext_match:
            formatted += f" доб.{ext_match.group(1)}"
        return formatted

    fixed_contacts = [contacts[0]]
    for row in contacts[1:]:
        if len(row) > 5:
            row[5] = format_single(row[5])
        fixed_contacts.append(row)

    return fixed_contacts

def fix_phones(contacts):
    return format_phone(contacts)