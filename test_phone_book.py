from unittest import TestCase

from phone_book import PhoneBook


class Test_phonebook(TestCase):

    def setUp(self):
        self.my_phone_book = PhoneBook()

    def tearDown(self):
        self.my_phone_book.contacts.clear()



    def test_create_contact_name(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertEqual(1, len(self.my_phone_book.contacts))

    def test_create_contact_number(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertEqual(1, len(self.my_phone_book.contacts))

    def test_delete_contact_name_is_valid(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.my_phone_book.deleteEntry("Bee_jay")
        self.assertEqual(0, len(self.my_phone_book.contacts))

    def test_delete_contact_name_is_invalid(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.my_phone_book.create_contact("Bee_jay 2", 2348165269245)

        self.assertEqual(2, len(self.my_phone_book.contacts))

    def test_search_contact_name_is_valid(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertTrue(self.my_phone_book.checkEntry("Bee_jay"))

    def test_search_contact_name_is_invalid(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.my_phone_book.deleteEntry("Bee_jay")
        self.assertFalse(self.my_phone_book.checkEntry("Bee_jay"))

    def test_that_i_can_add_contact_twice(self):
        self.my_phone_book.create_contact("Bee_jay", 2348165269244)
        self.assertEqual(1, len(self.my_phone_book.contacts))
        self.my_phone_book.create_contact("Mr_sikiru", 234806992338)
        self.assertEqual(2, len(self.my_phone_book.contacts))
