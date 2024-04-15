import unittest

from tests import DataExtractor


class DataExtractorTest(unittest.TestCase):
    def test_invalid_data(self):
        self.assertRaises(ValueError, DataExtractor.extract_data, '../input/invalid.csv')

    def test_extract_data(self):
        expected_result = [
            [6.0,   6.8,   -2.0,   8.2],
            [6.8,   23.14, -11.25, 22.11],
            [-2.0, -11.25,  50.5, -19.75],
            [8.2,   22.11, -19.75, 36.64],
            [983.0, 2896.0, 120.0, 138.0],
            [256.0, 485.0,  88.0,  61.0]
        ]
        self.assertEqual(DataExtractor.extract_data('../input/test2.csv'), expected_result)


if __name__ == '__main__':
    unittest.main()
