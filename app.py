from helpers import DataExtractor, EquationHelper, GaussianElimination
from models import Dataframe


def main():
    while True:
        var_str = input('Enter the number of independent variables: ')
        try:
            var_num = int(var_str)
            break
        except ValueError:
            print('Invalid number, please try again.')

    path = input('Enter the path to data file: ')

    try:
        data = DataExtractor(path).extract_data()
    except FileNotFoundError as e:
        print(e)
        exit(1)
    except ValueError as e:
        print(e)
        exit(2)
    dataframe = Dataframe(data=data)

    if not EquationHelper.dataframe_is_valid(df=dataframe, var_num=var_num):
        print('Invalid number of variables')
        exit(3)

    equation = EquationHelper.generate_equation(df=dataframe, var_num=var_num)
    ge = GaussianElimination(df=equation)

    roots = ge.find_roots()

    for key, value in roots.items():
        print('{0}: {1:.4f}'.format(key, value))


if __name__ == '__main__':
    main()