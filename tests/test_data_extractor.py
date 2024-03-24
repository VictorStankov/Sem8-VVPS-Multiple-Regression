import unittest

from tests import DataExtractor


class DataExtractorTest(unittest.TestCase):
    def test_invalid_path(self):
        de = DataExtractor('../input/missing.csv')
        self.assertRaises(FileNotFoundError, de.extract_data)

    def test_invalid_data(self):
        de = DataExtractor('../input/invalid.csv')
        self.assertRaises(ValueError, de.extract_data)


if __name__ == '__main__':
    unittest.main()
