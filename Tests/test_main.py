# pip install pytest
# python3 -m pytest


import pytest


from src.main import calculate_discount

def test_discount_for_underage():
    # AAA  - Arrange - Act - Assert
    age = 17
    expected = 10

    result = calculate_discount(age)

    assert result == expected

# @pytest.mark.xfail
@pytest.mark.skipif(True, reason='Не запускаем на боевом сервер')
def test_discount_for_adult():
    assert calculate_discount(18) == 1, 'Ошибка в вычислении скидки для возраста 18'

def test_discount_for_old_man():
    assert calculate_discount(80) == 15, 'Ошибка в вычислении скидки для возраста 80'


@pytest.mark.parametrize(
    'age,expected_discount',
    ((17, 10),
    (18, 0),
    (64, 0),
    (65, 15))
)
def test_calculate_discount_by_age(age, expected_discount):
    assert calculate_discount(age) == expected_discount, \
        f'Скидка для возраста {age} посчитана неправильно'