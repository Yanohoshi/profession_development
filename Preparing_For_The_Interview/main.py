# ========================================= Class Stack (Main function) ================================================
class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

# =================================================== Задача 2 =========================================================
def check_balance(brackets):
    stack = Stack()
    brackets_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    opening_brackets = set(brackets_dict.keys())
    closing_brackets = set(brackets_dict.values())

    for char in brackets:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False

            last_opening = stack.pop()

            if brackets_dict[last_opening] != char:
                return False

    return stack.is_empty()
# =================================================== Проверка =========================================================
if __name__ == "__main__":

    user_input = input("Введите строку со скобками для проверки: ")

    if check_balance(user_input):
        print("Сбалансированно")
    else:
        print("Несбалансировано")

# ================================================= Тест по умолчанию ==================================================
    # test_strings = [
    #     "((((([]))))))",
    #     "[([)])((([[[]]])))({}({}))",
    #     "{{{()}}}",
    #     "}{}",
    #     "{}{}",
    #     "[[(())]]"
    # ]
    #
    # print("Проверка тестовых примеров:")
    # for test in test_strings:
    #     result = check_balance(test)
    #     status = "Сбалансированно" if result else "Несбалансировано"
    #     print(f"'{test}' -> {status}")
    #
    # print("\n" + "=" * 50 + "\n")

# =============================================== Тест 1 задачи ========================================================

# if __name__ == "__main__":
#     stack = Stack()
#
# print("Стек пуст?", stack.is_empty())
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print("Размер стека:", stack.size())
# print("Верхний элемент:", stack.peek())
# print("Удаляем элемент:", stack.pop())
# print("Размер после удаления:", stack.size())
# print("Стек пуст?", stack.is_empty())