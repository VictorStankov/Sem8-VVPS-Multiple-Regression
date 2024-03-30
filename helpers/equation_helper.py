from models import Dataframe


class EquationHelper:

    @staticmethod
    def dataframe_is_valid(df: Dataframe) -> bool:
        return len(set([x for x in map(len, df.data)])) == 1

    @staticmethod
    def dataframe_variables_match(df: Dataframe, var_num: int) -> bool:
        return df.size[1] == var_num + 1

    @staticmethod
    def generate_equation(df: Dataframe, var_num: int) -> Dataframe:
        first_row = [df.size[0]]
        output = []

        for i in range(var_num + 1):
            first_row.extend([df.sum_column(i)])
        output.append(first_row)

        for i in range(var_num):
            row = [df.sum_column(i)]
            for j in range(var_num + 1):
                row.append(sum(df.multiply_columns(i, j)))
            output.append(row)

        return Dataframe(output)
