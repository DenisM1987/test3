# import os
from src.decorators import log


def test_log_to_console(capsys):
    """Тест вывода логов в консоль."""
    @log()
    def add(a, b):
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_to_file(tmp_path):
    """Тест записи логов в файл."""
    log_file = tmp_path / "test_log.txt"
    @log(filename=log_file)

def div(a, b):
        return a / b

    div(4, 2)
    with open(log_file, "r") as f:
        assert "div ok" in f.read()

    try:
        div(1, 0)
    except ZeroDivisionError:
        pass
    with open(log_file, "r") as f:
        content = f.read()
        assert "div error" in content
        assert "ZeroDivisionError" in content
