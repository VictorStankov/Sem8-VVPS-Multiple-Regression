from typing import Dict

from models import Dataframe


class GaussianElimination:
    """
    Helper class to perform Gaussian elimination.
    """
    def __init__(self, df: Dataframe):
        self.df = df

    def find_roots(self) -> Dict[int, float]:
        """
        Method that finds the roots of the diagonalised dataframe.
        :return: Dictionary with the roots of the diagonalised dataframe
        """
        output = {}  # Dictionary that stores the results
        diag_df = self.diagonalise()

        # Starting from the last row and going up, we find each root
        # After the root has been saved in the dictionary, it is used in subsequent calculations
        for i in range(diag_df.size[0] - 1, -1, -1):
            output[i] = diag_df[i][diag_df.size[1] - 1] - sum(
                [diag_df[i][x] * output.get(x, 1) for x in range(i + 1, diag_df.size[0])]
            )
        return output

    def diagonalise(self) -> Dataframe:
        """
        Method to perform diagonal elimination on a dataframe.
        :return: Diagonalised dataframe
        """
        for i in range(self.df.size[0]):
            # Divide row by itself, so we get 1 in the main diagonal
            self.df[i] = [x / self.df[i][i] for x in self.df[i]]

            # Multiply the row and subtract it from all the rows beneath it to ensure 0s below the main diagonal
            for j in range(i + 1, self.df.size[0]):
                row_subtract = [x * (-self.df[j][i]) for x in self.df[i]]
                self.df[j] = [self.df[j][x] + row_subtract[x] for x in range(len(row_subtract))]
        return self.df
