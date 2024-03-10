import unittest

from pistol_gun import PistolGun


class TestPistolGun(unittest.TestCase):

    def setUp(self):
        self.gun = PistolGun(9, 15)

    def test_load_bullets_beyond_capacity(self):
        with self.assertRaises(ValueError):
            self.gun.load_gun(20)

    def test_shoot_when_gun_is_empty(self):
        with self.assertRaises(ValueError):
            self.gun.shoot_gun()

    def test_toggle_safety_state(self):
        initial_safety_state = self.gun.safety_on
        self.gun.toggle_safety()
        self.assertNotEqual(initial_safety_state, self.gun.safety_on)
        self.gun.toggle_safety()
        self.assertEqual(initial_safety_state, self.gun.safety_on)

    def test_inspect_gun_state_after_loading_and_shooting(self):
        self.gun.toggle_safety()
        self.gun.load_gun(10)
        self.assertEqual(self.gun.inspect_gun(), "Caliber: 9,Capacity: 15,Ammo Count: 10,Safety: off")
        self.gun.shoot_gun()
        self.assertEqual(self.gun.inspect_gun(), "Caliber: 9,Capacity: 15,Ammo Count: 9,Safety: off")

    def test_initialize_with_invalid_caliber_or_capacity(self):
        with self.assertRaises(ValueError):
            PistolGun(-9, 15)
        with self.assertRaises(ValueError):
            PistolGun(9, 0)

    def test_load_bullets_with_negative_count(self):
        with self.assertRaises(ValueError):
            self.gun.load_gun(-5)

    def test_shoot_with_safety_on(self):
        with self.assertRaises(ValueError):
            self.gun.shoot_gun()

    def test_inspect_gun_state_with_safety_on_and_off(self):
        self.assertEqual(self.gun.inspect_gun(), "Caliber: 9,Capacity: 15,Ammo Count: 0,Safety: on")
        self.gun.toggle_safety()
        self.assertEqual(self.gun.inspect_gun(), "Caliber: 9,Capacity: 15,Ammo Count: 0,Safety: off")

    def test_toggle_safety_state_multiple_times(self):
        self.gun.toggle_safety()
        initial_safety_state = self.gun.safety_on
        for _ in range(5):
            self.assertEqual(initial_safety_state, self.gun.safety_on)

    def test_shoot_bullets_beyond_capacity(self):
        self.gun.toggle_safety()
        self.gun.load_gun(15)
        for _ in range(15):
            self.gun.shoot_gun()
        self.assertEqual(self.gun.ammo_count, 0)
