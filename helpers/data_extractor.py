from typing import List


class DataExtractor:
    def __init__(self, path: str):
        self.path = path

    def extract_data(self) -> List[List[float]]:
        output = []
        try:
            with open(self.path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    output.append([float(x) for x in line.strip().split(',')])
        except FileNotFoundError:
            raise FileNotFoundError('File not found.')
        except ValueError:
            raise ValueError('Invalid data in input file.')

        return output
