import functools
def log(filename=None):
    """Декоратор, который логирует результат или ошибку выполнения функции."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Пытаемся выполнить функцию
                result = func(*args, **kwargs)
                #Если все True, формируем сообщение
                log_msg = f"{func.__name__} ok"

                # Записываем лог
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                else:
                    print(log_msg)

                return result

            except Exception as e:
        # Если возникла ошибка, формируем подробное сообщение
                log_msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

        # Записываем лог ошибки
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_msg + "\n")
            else:
                print(log_msg)

            # Пробрасываем ошибку дальше, чтобы программа знала о ней
            raise e

        return wrapper
    return decorator