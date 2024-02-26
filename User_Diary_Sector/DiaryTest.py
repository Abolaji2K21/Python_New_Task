import unittest
from User_Diary_Sector import Diary



class DiaryTest(unittest.TestCase):

    def test_that_i_can_create_a_diary(self):
        username = "Bee jay"
        password = "password@"
        my_diary = Diary(username, password)

        self.assertEqual(username, my_diary.get_username())
        self.assertEqual(password, my_diary.get_password())

    def test_that_i_cant_create_a_diary_without_a_username(self):
        with self.assertRaises(ValueError):
            Diary(None, "password")

    def test_that_i_cant_create_a_diary_without_a_password(self):
        with self.assertRaises(ValueError):
            Diary("Bee jay", None)

    def test_that_the_diary_is_locked(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())

    def test_that_the_unlock_features_work_on_my_diary_with_a_correct_passkey(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

    def test_that_the_unlock_feature_works_on_my_diary_with_an_incorrect_passkey(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        with self.assertRaises(InvalidPinException):
            my_diary.unlock_diary("password")

    def test_that_create_entry_feature_works(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

        id = 1
        title = "How To Start Thinking"
        body = "Hello and how you doing today ? i am documenting my findings because i need to start thinking "

        my_diary.create_entry(id, title, body)
        self.assertEqual(1, my_diary.get_number_of_entry())

    def test_find_entry_by_id_feature(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

        id1 = 1
        title1 = "How To Start Thinking"
        body1 = "Hello and how you doing today? I am documenting my findings because I need to start thinking."

        my_diary.create_entry(id1, title1, body1)
        self.assertEqual(1, my_diary.get_number_of_entry())

        id2 = 2
        title2 = "How To Stop Thinking"
        body2 = "Hello and how you doing today? I am documenting my findings because I need to stop thinking."

        my_diary.create_entry(id2, title2, body2)
        self.assertEqual(2, my_diary.get_number_of_entry())

        found_entry1 = my_diary.find_entry_by_id(1)
        self.assertIsNotNone(found_entry1)
        self.assertEqual(1, found_entry1.id)

        found_entry2 = my_diary.find_entry_by_id(2)
        self.assertIsNotNone(found_entry2)
        self.assertEqual(2, found_entry2.id)

    def test_that_remove_entry_by_id_feature_works(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

        id = 1
        title = "How To Start Thinking"
        body = "Hello and how you doing today ? i am documenting my findings because i need to start thinking "

        my_diary.create_entry(id, title, body)
        self.assertEqual(1, my_diary.get_number_of_entry())

        id1 = 2
        title1 = "How To Stop Thinking"
        body1 = "Hello and how you doing today ? i am documenting my findings because i need to stop thinking "

        my_diary.create_entry(id1, title1, body1)
        self.assertEqual(2, my_diary.get_number_of_entry())

        found_entry = my_diary.find_entry_by_id(2)
        self.assertEqual(2, found_entry.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(2))

        found_entry1 = my_diary.find_entry_by_id(1)
        self.assertEqual(1, found_entry1.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(1))

        my_diary.delete_entry(2)
        self.assertEqual(1, my_diary.get_number_of_entry())

        my_diary.delete_entry(1)
        self.assertEqual(0, my_diary.get_number_of_entry())

    def test_that_update_entry_by_id_feature_works(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

        id = 1
        title = "How To Start Thinking"
        body = "Hello and how you doing today ? i am documenting my findings because i need to start thinking "

        my_diary.create_entry(id, title, body)
        self.assertEqual(1, my_diary.get_number_of_entry())

        id1 = 2
        title1 = "How To Stop Thinking"
        body1 = "Hello and how you doing today ? i am documenting my findings because i need to stop thinking "

        my_diary.create_entry(id1, title1, body1)
        self.assertEqual(2, my_diary.get_number_of_entry())

        found_entry = my_diary.find_entry_by_id(2)
        self.assertEqual(2, found_entry.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(2))

        found_entry1 = my_diary.find_entry_by_id(1)
        self.assertEqual(1, found_entry1.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(1))

        new_title = "NewTitle"
        new_body = "NewBody"
        my_diary.update_entry(1, new_title, new_body)

        updated_entry = my_diary.find_entry_by_id(1)
        self.assertEqual(new_title, updated_entry.title)
        self.assertEqual(new_body, updated_entry.body)

        updated_title = "NewTitle"
        updated_body = "NewBody"
        my_diary.update_entry(2, updated_title, updated_body)

        my_diary_entry_by_id_entry = my_diary.find_entry_by_id(2)
        self.assertEqual(updated_title, my_diary_entry_by_id_entry.title)
        self.assertEqual(updated_body, my_diary_entry_by_id_entry.body)

    def test_that_update_entry_by_id_feature_works_and_i_cant_update_a_non_existing_entry(self):
        username = "Bee jay"
        password = "password@"

        my_diary = Diary(username, password)
        self.assertTrue(my_diary.is_locked())
        my_diary.unlock_diary("password@")
        self.assertFalse(my_diary.is_locked())

        id = 1
        title = "How To Start Thinking"
        body = "Hello and how you doing today ? i am documenting my findings because i need to start thinking "

        my_diary.create_entry(id, title, body)
        self.assertEqual(1, my_diary.get_number_of_entry())

        id1 = 2
        title1 = "How To Stop Thinking"
        body1 = "Hello and how you doing today ? i am documenting my findings because i need to stop thinking "

        my_diary.create_entry(id1, title1, body1)
        self.assertEqual(2, my_diary.get_number_of_entry())

        found_entry = my_diary.find_entry_by_id(2)
        self.assertEqual(2, found_entry.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(2))

        found_entry1 = my_diary.find_entry_by_id(1)
        self.assertEqual(1, found_entry1.id)
        self.assertIsNotNone(my_diary.find_entry_by_id(1))

        new_title = "NewTitle"
        new_body = "NewBody"
        my_diary.update_entry(1, new_title, new_body)

        updated_entry = my_diary.find_entry_by_id(1)
        self.assertEqual(new_title, updated_entry.title)
        self.assertEqual(new_body, updated_entry.body)

        updated_title = "NewTitle"
        updated_body = "NewBody"
        my_diary.update_entry(2, updated_title, updated_body)

        my_diary_entry_by_id_entry = my_diary.find_entry_by_id(2)
        self.assertEqual(updated_title, my_diary_entry_by_id_entry.title)
        self.assertEqual(updated_body, my_diary_entry_by_id_entry.body)

        fake_title = "NewTitle"
        fake_body = "NewBody"
        with self.assertRaises(KeyError):
            my_diary.update_entry(3, fake_title, fake_body)
