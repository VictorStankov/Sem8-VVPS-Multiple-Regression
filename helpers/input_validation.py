import os


class InputValidation:
    """
    Helper class to validate input data.
    """
    @staticmethod
    def is_variable_number_valid(var: str) -> bool:
        try:
            if int(var) >= 2:
                return True
            return False
        except ValueError:
            return False

    @staticmethod
    def is_path_valid(path: str) -> bool:
        return os.path.exists(path)
