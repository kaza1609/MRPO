import unittest
from models import *


class TestValidateName(unittest.TestCase):
    def test_valid_name(self):
        names = ['Mona', 'Igorevna']
        for name in names:
            self.assertTrue(validate_name(name))

    def test_invalid_name(self):
        names = ['123', '1MONA', 'Test^', 'ABC123']
        with self.assertRaises(Exception):
            for name in names:
                validate_name(name)


class TestValidateNonNegative(unittest.TestCase):
    def test_valid_numbers(self):
        numbers = [1, 10, 160.5]
        for number in numbers:
            self.assertTrue(validate_non_negative_number(number))

    def test_invalid_numbers(self):
        numbers = [10, -160, 0]
        with self.assertRaises(Exception):
            for number in numbers:
                validate_non_negative_number(number)


class TestValidateDate(unittest.TestCase):
    def test_valid_date(self):
        dates = [
            datetime(2023, 11, 13, 1, 13),
            datetime(2023, 10, 13, 1, 13)
        ]
        for date in dates:
            self.assertTrue(validate_date(date))

    def test_invalid_date(self):
        dates = [
            datetime(2025, 11, 13, 1, 13),
            datetime(2025, 10, 13, 1, 13)
        ]
        with self.assertRaises(Exception):
            for date in dates:
                validate_date(date)


class TestValidateGender(unittest.TestCase):
    def test_valid_gender(self):
        genders = ['м', 'ж']
        for gender in genders:
            self.assertTrue(validate_gender(gender))

    def test_invalid_gender(self):
        genders = ['вертолет', 'мона']
        with self.assertRaises(Exception):
            for gender in genders:
                validate_gender(gender)
