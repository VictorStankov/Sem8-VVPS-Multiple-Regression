import unittest

from tests import EquationHelper, Dataframe


class EquationHelperTest(unittest.TestCase):
    def test_dataframe_is_valid(self):
        data = Dataframe([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(EquationHelper.dataframe_is_valid(df=data, var_num=2), True)

    def test_dataframe_is_invalid(self):
        data = Dataframe([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(EquationHelper.dataframe_is_valid(df=data, var_num=3), False)

    def test_invalid_data(self):
        data = Dataframe(data=[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]
        ])
        expected_result = Dataframe(data=[
            [6, 66, 72, 78, 84],
            [66, 1006, 1072, 1138, 1204],
            [72, 1072, 1144, 1216, 1288],
            [78, 1138, 1216, 1294, 1372]
        ])

        self.assertEqual(EquationHelper.generate_equation(df=data, var_num=3).data, expected_result.data)


if __name__ == '__main__':
    unittest.main()
