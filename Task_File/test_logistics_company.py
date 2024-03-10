from unittest import TestCase

import unittest
from logistics_company import logistics_company, InvalidDeliveriesException


class TestLogisticsCompany(unittest.TestCase):

    def setUp(self):
        self.company = logistics_company()

    def test_successful_deliveries_below_0(self):
        successfulDeliveries = -10
        with self.assertRaises(InvalidDeliveriesException):
            self.company.calculate_commission(successfulDeliveries)

    def test_successful_deliveries_between_0_and_49(self):
        self.assertEqual(self.company.calculate_commission(49), 12840)

    def test_successful_deliveries_between_50_and_59(self):
        self.assertEqual(self.company.calculate_commission(50), 15000)

    def test_successful_deliveries_between_60_and_69(self):
        self.assertEqual(self.company.calculate_commission(60), 20000)

    def test_successful_deliveries_between_70_and_99(self):
        self.assertEqual(self.company.calculate_commission(70), 40000)

    def test_successful_deliveries_above_100(self):
        with self.assertRaises(InvalidDeliveriesException):
            self.company.calculate_commission(101)
