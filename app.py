from helpers import DataExtractor, EquationHelper, GaussianElimination, InputValidation
from models import Dataframe


def main():
    var_num = 0

    while True:
        var_str = input('Enter the number of independent variables: ')
        if not InputValidation.is_variable_number_valid(var=var_str):
            print('Invalid number, please enter a whole number greater than 1.')
            continue

        var_num = int(var_str)
        break

    while True:
        path = input('Enter the path to data file: ')

        if not InputValidation.is_path_valid(path=path):
            print('Input file could not be accessed. Please try again.')
            continue

        break

    try:
        data = DataExtractor.extract_data(path)
    except ValueError as e:
        print(e)
        exit(1)

    dataframe = Dataframe(data=data)

    if not EquationHelper.dataframe_is_valid(df=dataframe):
        print('Input file has missing values.')
        exit(2)

    if not EquationHelper.dataframe_variables_match(df=dataframe, var_num=var_num):
        print('Invalid number of variables.')
        exit(3)

    equation = EquationHelper.generate_equation(df=dataframe, var_num=var_num)
    ge = GaussianElimination(df=equation)

    roots = ge.find_roots()

    for key, value in reversed(roots.items()):
        print(f'b{key}: {value:.5f}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(-1)
