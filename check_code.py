#!/usr/bin/env python3
"""Скрипт для проверки качества кода."""

import subprocess
import sys
from typing import List


def run_command(command: List[str], description: str) -> bool:
    """Запускает команду и возвращает True если успешно."""
    print(f"\nОписание: {description}")
    print(f"Команда: {' '.join(command)}")

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("[ + ] Успешно")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("[ - ] Ошибка")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False


def main() -> None:
    """Главная функция."""
    print("[!] Проверка качества кода")

    # Сначала проверяем через pre-commit (это покрывает все инструменты)
    checks = [
        (["pre-commit", "run", "--all-files"], "Запуск всех pre-commit хуков"),
    ]

    # запуск инструмента по отдельности
    # checks = [
    #     (["black", "--check", "."], "Проверка форматирования (black)"),
    #     (["isort", "--check-only", "."], "Проверка импортов (isort)"),
    #     (["flake8", "."], "Проверка стиля кода (flake8)"),
    #     (["mypy", "."], "Проверка типов (mypy)"),
    # ]

    all_passed = True

    for command, description in checks:
        if not run_command(command, description):
            all_passed = False

    if all_passed:
        print("\n[!] Все проверки прошли успешно!")
        sys.exit(0)
    else:
        print("\n[!] Некоторые проверки не прошли")
        print("Для исправления запустите:")
        print("  black .")
        print("  isort .")
        print("  pre-commit run --all-files")
        sys.exit(1)


if __name__ == "__main__":
    main()
