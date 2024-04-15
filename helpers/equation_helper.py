from models import Dataframe


class EquationHelper:
    """
    Helper class for equation calculations.
    """
    @staticmethod
    def dataframe_is_valid(df: Dataframe) -> bool:
        """
        Methods that checks if all rows contain the same amount of columns.
        :param df: Dataframe to check
        :return: boolean
        """
        return len(set([x for x in map(len, df.data)])) == 1

    @staticmethod
    def dataframe_variables_match(df: Dataframe, var_num: int) -> bool:
        """
        Method that checks if the dataframe matches the number of independent variables supplied by the user.
        :param df: Dataframe to check
        :param var_num: Number of independent variables
        :return: boolean
        """
        return df.size[1] == var_num + 1

    @staticmethod
    def generate_equation(df: Dataframe, var_num: int) -> Dataframe:
        """
        Method that generates an equation based used for calculating the roots of the multiple regression of a
        system of equations.
        :param df: Dataframe containing the system of equation in matrix form
        :param var_num: Number of independent variables
        :return: Dataframe containing the equation for finding the roots of the multiple regression in matrix form
        """
        first_row = [df.size[0]]
        output = []

        for i in range(var_num + 1):  # Calculating the first row separately as the rest of the rows follow a pattern
            first_row.extend([df.sum_column(i)])
        output.append(first_row)

        for i in range(var_num):
            row = [df.sum_column(i)]
            for j in range(var_num + 1):
                row.append(sum(df.multiply_columns(i, j)))
            output.append(row)

        return Dataframe(output)
