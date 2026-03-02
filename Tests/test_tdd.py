# длина пароля не меньше 8 символов
# цифры
# заглавные и прописные буквы
# пунктуационные символы

from src.tdd import is_strong_password

def test_password_is_strong():
    assert is_strong_password('aA12;"Sd')

def test_short_password_is_weak():
    assert is_strong_password('aF2;sdE') is False

def test_password_without_digits_is_weak():
    assert is_strong_password('asASF!:dsgsdg') is False

def test_password_without_capital_is_weak():
    assert is_strong_password('af2;sdedfh') is False

def test_password_without_lower_is_weak():
    assert is_strong_password('AF2;SDLGKE') is False

def test_password_without_punctuation_is_weak():
    assert is_strong_password('aF234sdE') is False

