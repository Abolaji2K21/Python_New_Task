import unittest

from PistolGun import PistolGun


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.my_gun = PistolGun("9mm", 20)


    def tearDown(self):
        self.my_gun = None

    def test_gun_capacity_is_20(self):
        expected = 20
        actual = self.my_gun.capacity
        self.assertEqual(expected, actual)

    def test_gun_caliber_is_9mm(self):
        expected = "9mm"
        actual = self.my_gun.caliber
        self.assertEqual(expected, actual)

    def test_that_my_gun_can_be_loaded(self):
        self.my_gun.load_gun(10)
        self.assertEqual(10, self.my_gun.ammo_count)

    def test_that_my_gun_can_not_be_loaded_with_a_negative_number(self):
        self.my_gun.load_gun(-10)
        self.assertEqual(0, self.my_gun.ammo_count)

    def test_that_my_gun_my_gun_can_shoot(self):
        self.my_gun.load_gun(15)
        self.assertEqual(15, self.my_gun.ammo_count)
        self.my_gun.shoot_gun()
        self.assertEqual(14, self.my_gun.ammo_count)

    def test_that_my_gun_my_gun_can_shoot_twice(self):
        self.my_gun.load_gun(15)
        self.assertEqual(15, self.my_gun.ammo_count)
        self.my_gun.shoot_gun()
        self.my_gun.shoot_gun()
        self.my_gun.shoot_gun()
        self.assertEqual(12, self.my_gun.ammo_count)

    def test_that_my_gun_can_not_be_loaded_more_than_it_capacity(self):
        self.my_gun.load_gun(21)
        self.assertEqual(20, self.my_gun.capacity)


