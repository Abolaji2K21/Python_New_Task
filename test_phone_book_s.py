from unittest import TestCase

from phone_book_s import PhoneBook_s


class Test_phonebook_s(TestCase):


    def setUp(self):
        self.my_phone_book = PhoneBook_s()

    def tearDown(self):
        self.my_phone_book.contactName.clear()
        self.my_phone_book.contactNumber.clear()




    def test_create_contact_name(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertEqual(1, len(self.my_phone_book.contactName))

    def test_create_contact_number(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertEqual(1, len(self.my_phone_book.contactNumber))

    def test_delete_contact_name(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.my_phone_book.deleteEntry("Bee_jay")
        self.assertEqual(0, len(self.my_phone_book.contactName))

    def test_search_contact_name(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertTrue(self.my_phone_book.checkEntry("Bee_jay"))

    def test_search_contact_name_is_invalid(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.my_phone_book.deleteEntry("Bee_jay")
        self.assertFalse(self.my_phone_book.checkEntry("Bee_jay"))

