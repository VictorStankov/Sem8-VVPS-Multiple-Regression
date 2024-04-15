import unittest

from tests import InputValidation


class InputValidationTest(unittest.TestCase):
    def test_is_variable_number_valid(self):
        self.assertTrue(InputValidation.is_variable_number_valid('2'))
        self.assertTrue(InputValidation.is_variable_number_valid('10'))
        self.assertFalse(InputValidation.is_variable_number_valid('1'))
        self.assertFalse(InputValidation.is_variable_number_valid('4.5'))
        self.assertFalse(InputValidation.is_variable_number_valid('Invalid Input'))

    def test_is_path_valid(self):
        self.assertTrue(InputValidation.is_path_valid('../input/example.csv'))
        self.assertFalse(InputValidation.is_path_valid('../input/missing.csv'))


if __name__ == '__main__':
    unittest.main()
