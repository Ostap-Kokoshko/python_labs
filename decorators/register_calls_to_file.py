import functools


def register_calls_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        method_name = func.__name__
        call_count = getattr(wrapper, f"_{method_name}_call_count", 0)

        if call_count == 0:
            with open("call_counts.txt", "a") as file:
                file.write(f"{method_name}: 1\n")
        else:
            with open("call_counts.txt", "r+") as file:
                lines = file.readlines()
                file.seek(0)
                for line in lines:
                    if line.startswith(f"{method_name}:"):
                        count = int(line.split(":")[1]) + 1
                        line = f"{method_name}: {count}\n"
                    file.write(line)
                file.truncate()

        setattr(wrapper, f"_{method_name}_call_count", call_count + 1)
        return func(*args, **kwargs)

    return wrapper
