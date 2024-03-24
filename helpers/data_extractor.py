from typing import List


class DataExtractor:
    def __init__(self, path: str):
        self.path = path

    def extract_data(self) -> List[List[float]]:
        output = []
        try:
            file = open(self.path, 'r')
            lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError('File not found.')

        try:
            for line in lines:
                output.append([float(x) for x in line.strip().split(',')])

            file.close()
        except ValueError:
            file.close()
            raise ValueError('Invalid data in input file.')

        return output
