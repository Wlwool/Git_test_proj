# README

![Code Quality](https://github.com/ваш-username/ваш-репозиторий/workflows/Code%20Quality%20Checks/badge.svg)

```

## Расширенная версия с матрицей Python версий

```yaml:.github/workflows/checks.yml
name: Code Quality Checks

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  code-quality:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.11', '3.12', '3.13']

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install black isort flake8 mypy

    - name: Run checks
      run: |
        black --check .
        isort --check-only .
        flake8 .
        mypy . --ignore-missing-imports
```
