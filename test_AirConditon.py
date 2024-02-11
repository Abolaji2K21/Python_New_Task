from unittest import TestCase
from AirCondition import AirCondition


class Test_AirCondition(TestCase):
    def setUp(self):
        self.my_ac = AirCondition()
        self.my_ac.set_ac_on(True)

    def tearDown(self):
        self.my_ac.set_ac_off(True)
        self.my_ac.set_ac_temp(16)

    def test_that_when_ac_is_on_it_is_on(self):
        self.my_ac.set_ac_on(True)
        self.assertTrue(self.my_ac.get_ac_on())

    def test_that_when_ac_is_on_it_is_not_off(self):
        self.my_ac.set_ac_on(True)
        self.assertFalse(self.my_ac.get_ac_off())

    def test_that_when_ac_is_on_default_temp_occurs(self):
        self.my_ac.set_ac_on(True)
        expected = 16
        actual = self.my_ac.get_ac_temp()
        self.assertEqual(expected, actual)

    def test_that_when_ac_is_off_it_is_indeed_off(self):
        self.my_ac.set_ac_off(True)
        self.assertTrue(self.my_ac.get_ac_off())

    def test_that_when_ac_is_off_it_is_not_on(self):
        self.my_ac.set_ac_off(True)
        self.assertTrue(self.my_ac.get_ac_on())

    def test_that_when_ac_is_off_temp_is_indeed_at_intial(self):
        self.my_ac.set_ac_off(True)
        expected_temp = 16
        actual_temp = self.my_ac.get_ac_temp()
        self.assertEqual(expected_temp, actual_temp)
