"""шаблон:
Объект + is/are + глагол в 3-й форме + by + инструмент.
Пример:
The container (объект) is started (действие) by Docker (инструмент).
"The port is exposed by the EXPOSE instruction."
"""

1. The Environment variables is set by ENV
EXPOSE - The port is described by your application

2. Docker instructions is run by Dockerfile in order.
The following unknowndirective is treated as a comment because it isn't recognized
Non line-breaking whitespace is permitted in a parser directive

3. Dockerfile
FROM python:3.13-slim # The base image if python 3.13-slim

RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*  # set timezone
ENV TZ=Europe/Moscow    # set timezone

WORKDIR /app # The current working directory

ENV PYTHONPATH=/app # The python path

COPY requirements.txt .  # The file that contains the all dependencies

RUN pip install --no-cache-dir -r requirements.txt  # install dependencies from requirements.txt

COPY . .  # copy all files in the current directory to the current working directory

CMD ["python", "main.py"]  # Run the command when the container is started