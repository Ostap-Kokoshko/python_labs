def register_calls_to_file(func):
    call_count = 0

    def wrapper(*args, **kwargs):
        method_name = func.__name__
        nonlocal call_count
        with open("call_counts.txt", "r+") as file:
            file.write(f"{method_name}: {call_count + 1}\n")
            call_count += 1
        return func(*args, **kwargs)
    return wrapper
