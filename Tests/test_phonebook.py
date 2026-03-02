from src.phonebook import PhoneBook

class TestPhonbook:
    def test_create_empty_phonebook(self, empty_phonebook):
        assert len(empty_phonebook.get_all_contacts()) == 0


    def test_add_new_contact(self, empty_phonebook):
        empty_phonebook.add_contact('Мама', 124124124)
        assert len(empty_phonebook.get_all_contacts()) == 1


    def test_add_few_contacts(self, empty_phonebook):
        empty_phonebook.add_contact('Мама', 124124124)
        empty_phonebook.add_contact('папа', 999999999)
        empty_phonebook.add_contact('братан', 345345623)
        assert len(empty_phonebook.get_all_contacts()) == 3


    def test_add_exist_contact(self, empty_phonebook):
        empty_phonebook.add_contact('Мама', 124124124)
        empty_phonebook.add_contact('Мама', 124124124)
        assert len(empty_phonebook.get_all_contacts()) == 1

    def test_find_exist_contact(self, non_empty_phonebook):
        assert non_empty_phonebook.find_contact('папа') == 999999999

    def test_find_non_exist_contact(self, non_empty_phonebook):
        assert non_empty_phonebook.find_contact('Жора') is None