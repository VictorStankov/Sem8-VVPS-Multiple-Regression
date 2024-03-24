from typing import Dict

from models import Dataframe


class GaussianElimination:
    def __init__(self, df: Dataframe):
        self.df = df

    def find_roots(self) -> Dict[int, float]:
        output = {}
        diag_df = self.diagonalise()
        for i in range(diag_df.size[0] - 1, -1, -1):
            output[i] = diag_df[i][diag_df.size[1] - 1] - sum(
                [diag_df[i][x] * output.get(x, 1) for x in range(i + 1, diag_df.size[0])]
            )
        return output

    def diagonalise(self) -> Dataframe:
        for i in range(self.df.size[0]):
            self.df[i] = [x / self.df[i][i] for x in self.df[i]]
            for j in range(i + 1, self.df.size[0]):
                row_subtract = [x * (-self.df[j][i]) for x in self.df[i]]
                self.df[j] = [self.df[j][x] + row_subtract[x] for x in range(len(row_subtract))]
        return self.df

