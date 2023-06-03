import os


def save_result_to_file(func):
    def wrapper(self, *args, **kwargs):
        class_name = self.__class__.__name__
        method_name = func.__name__
        filename = f"{class_name}_{method_name}.txt"

        if os.path.exists(filename):
            mode = 'a'
        else:
            mode = 'w'

        with open(filename, mode) as file:
            result = func(self, *args, **kwargs)
            file.write(str(result) + '\n')
        return result
    return wrapper
