import pytest
from src.decorators import log


def test_log_to_console(capsys):
    """Тест вывода в консоль."""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert "add ok" in captured.out
    assert "error" not in captured.out


def test_log_to_file(tmp_path):
    """Тест записи в файл."""
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def div(a: int, b: int) -> float:
        return a / b

    # Проверка успешного выполнения
    div(10, 2)
    with open(log_file, "r") as f:
        content = f.read()
        assert "div ok" in content
        assert "error" not in content

    # Проверка ошибки
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
    with open(log_file, "r") as f:
        content = f.read()
        assert "ZeroDivisionError" in content
        assert "Inputs: (1, 0)" in content
