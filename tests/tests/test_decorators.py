import pytest
import os
from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест успешного логирования в консоль."""

    @log()
    def multiply(x, y):
        return x * y

    multiply(2, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "multiply ok"


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль."""

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (10, 0), {}" in captured.out


def test_log_to_file_success():
    """Тест записи лога в файл."""
    filename = "test_log.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename=filename)
    def greet(name):
        return f"Hello, {name}"

    greet("Alice")

    with open(filename, "r") as f:
        log_content = f.read().strip()

    assert log_content == "greet ok"

    # Удаляем временный файл после теста
    os.remove(filename)


def test_log_to_file_error():
    """Тест записи ошибки в файл."""
    filename = "error_log.txt"

    @log(filename=filename)
    def fail_func():
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        fail_func()

    with open(filename, "r") as f:
        log_content = f.read().strip()

    assert "fail_func error: ValueError" in log_content

    os.remove(filename)
