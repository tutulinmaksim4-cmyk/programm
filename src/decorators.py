import functools


def log(filename=None):
    """Декоратор, который логирует результат или ошибку выполнения функции."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_msg = f"{func.__name__} ok"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                return result

            except Exception as e:
                log_msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                raise e

        return wrapper

    return decorator
