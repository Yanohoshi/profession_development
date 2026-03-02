import pytest


from src.phonebook import PhoneBook


@pytest.fixture
def empty_phonebook():
    phonebook = PhoneBook()
    yield phonebook
    del phonebook


@pytest.fixture
def non_empty_phonebook():
    phonebook = PhoneBook()
    phonebook.add_contact('Мама', 124124124)
    phonebook.add_contact('папа', 999999999)
    phonebook.add_contact('братан', 345345623)
    phonebook.add_contact('Васек', 457373434)
    yield phonebook
    del phonebook