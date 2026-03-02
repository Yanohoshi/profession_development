import pytest

from src.les1 import check_age
from src.les2 import solve
from src.les3 import solve2

@pytest.mark.parametrize(
    'age, expected',
    ((12, 'Доступ запрещён'),
     (18, 'Доступ разрешён'),
     (25, 'Доступ разрешён'))
)
def test_check_age(age, expected):
    assert check_age(age) == expected, f'Получен ответ {expected}.'

@pytest.mark.parametrize('boys, girls, expected',
    (
        (
            ['Peter', 'Alex', 'John', 'Arthur', 'Richard'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            'Alex и Emma, Arthur и Kate, John и Kira, Peter и Liza, Richard и Trisha'),
        (
            ['Peter', 'Alex', 'John', 'Arthur'],
            ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'],
            "Кто-то может остаться без пары!"
        )
    )
)
def test_solve(boys, girls, expected):
    assert solve(boys, girls) == expected, f"Знакомство не удалось: {expected}"

@pytest.mark.parametrize('phrases,expected',[
    (
        ["нажал кабан на баклажан",
            "дом как комод",
            "рвал дед лавр",
            "азот калий и лактоза",
            "а собака боса",
            "тонет енот",
            "карман мрак",
            "пуст суп"],

         ["нажал кабан на баклажан",
             "рвал дед лавр",
             "азот калий и лактоза",
             "а собака боса",
             "тонет енот",
             "пуст суп"],
    )
])
def test_solve_2(phrases, expected):
    assert solve2(phrases) == expected, f"Неверный результат: {expected}"