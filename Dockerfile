FROM python:3.10-slim
# System dependencies are updated and the timezone is configured
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*
# The timezone is set to Europe/Moscow
ENV TZ=Europe/Moscow
# The working directory is created and set to /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
