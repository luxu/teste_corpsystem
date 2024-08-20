FROM python:3.12-slim

WORKDIR /app

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", ":8000", "core.wsgi" ]