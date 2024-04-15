from typing import List


class DataExtractor:
    """
    Static class for extracting input data from a csv file.
    """
    @staticmethod
    def extract_data(path: str) -> List[List[float]]:
        output = []
        try:
            with open(path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    output.append([float(x) for x in line.strip().split(',')])
        except ValueError:
            raise ValueError('Invalid data in input file.')

        return output
