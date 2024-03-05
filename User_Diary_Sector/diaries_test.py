import unittest

from User_Diary_Sector import diary
from User_Diary_Sector.diaries import Diaries


class MyTestCase(unittest.TestCase):
    def test_the_number_of_diaries(self):
        my_diaries = Diaries()
        self.assertEqual(0, my_diaries.get_number_of_diaries())

    def test_that_i_can_add_a_diary(self):
        my_diaries = Diaries()
        my_diaries.add_diary('username', 'password')
        actual = my_diaries.get_number_of_diaries()
        self.assertEqual(1, actual)

    def test_that_i_can_add_to_my_diary_more_than_once_and_it_increase(self):
        my_diaries = Diaries()
        my_diaries.add_diary('username', 'password')
        my_diaries.add_diary('username@', 'password@')
        actual = my_diaries.get_number_of_diaries()
        self.assertEqual(2, actual)

    def test_that_i_can_find_a_diary(self):
        my_diaries = Diaries()
        my_diaries.add_diary('username', 'password')
        found_diary = my_diaries.find_by_username("username")
        self.assertIsNotNone(found_diary)
        self.assertEqual("username", found_diary.get_username())
        actual = my_diaries.get_number_of_diaries()
        self.assertEqual(1, actual)

    def test_that_i_can_delete_diary(self):
        my_diaries = Diaries()
        my_diaries.add_diary('username', 'password')
        my_diaries.delete_diary('username', 'password')
        actual = my_diaries.get_number_of_diaries()
        self.assertEqual(0, actual)
