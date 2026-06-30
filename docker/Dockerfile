FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    network-manager \
    iproute2 \
    iputils-ping \
    wireless-tools \
    iw \
    ethtool \
    dbus \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "backend/app.py"]