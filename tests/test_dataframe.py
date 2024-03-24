import unittest

from tests import Dataframe


class DataframeTest(unittest.TestCase):
    def setUp(self):
        self.data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.df = Dataframe(self.data)

    def test_size(self):
        self.assertEqual(self.df.size, (4, 3))

    def test_get_row(self):
        self.assertEqual(self.df[0], [1, 2, 3])

    def test_set_row(self):
        self.df[1] = [12, 18, 31]

        self.assertEqual(self.df[1], [12, 18, 31])

    def test_get_column(self):
        self.assertEqual(self.df.get_column(2), [3, 6, 9, 12])

    def test_sum_column(self):
        self.assertEqual(self.df.sum_column(1), 26)

    def test_multiply_columns(self):
        self.assertEqual(self.df.multiply_columns(0, 1), [2, 20, 56, 110])


if __name__ == '__main__':
    unittest.main()
