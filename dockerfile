FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev-compat \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

RUN pip install --no-cache-dir Django mysqlclient

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
