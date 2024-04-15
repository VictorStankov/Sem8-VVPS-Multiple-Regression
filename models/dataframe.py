from typing import List


class Dataframe:
    """
    Class representing a dataframe structure.
    """
    def __init__(self, data: List[List[float]]):
        self.size = (len(data), max(map(len, data)))
        self.data = data

    def __getitem__(self, key: int):
        return self.data[key]

    def __setitem__(self, key: int, value: List[float]):
        self.data[key] = value

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.data)

    def get_column(self, col_index: int):
        return [self.data[x][col_index] for x in range(self.size[0])]

    def sum_column(self, col_index: int):
        return sum(self.get_column(col_index=col_index))

    def multiply_columns(self, col_index1: int, col_index2: int):
        return [self.data[x][col_index1] * self.data[x][col_index2] for x in range(self.size[0])]
