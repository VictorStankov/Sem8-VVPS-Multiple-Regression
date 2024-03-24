import unittest

from tests import GaussianElimination, Dataframe, DataExtractor, EquationHelper


class GaussianEliminationTest(unittest.TestCase):
    def setUp(self):
        data = DataExtractor('../input/test1.csv').extract_data()
        df = Dataframe(data=data)

        self.equation = EquationHelper.generate_equation(df=df, var_num=3)

    def test_diagonalise(self):
        expected_result = [
            [1.0, 278.3333333333333, 59.166666666666664, 24.833333333333332, 23.016666666666666],
            [0.0, 1.0, 0.08627687437583616, -0.03378492962258105, 0.06097831207250669],
            [0.0, 0.0, 1.0, 0.5211391775308692, 0.08743610417739194],
            [0.0, 0.0, 0.0, 1.0, 0.15104864761036024]
        ]

        ge = GaussianElimination(df=self.equation)
        self.assertEqual(ge.diagonalise().data, expected_result)

    def test_invalid_data(self):
        expected_result = {
            0: 0.5664574696019535,
            1: 0.06532925469423304,
            2: 0.008718736194578705,
            3: 0.15104864761036024
        }

        ge = GaussianElimination(df=self.equation)
        self.assertEqual(ge.find_roots(), expected_result)


if __name__ == '__main__':
    unittest.main()
