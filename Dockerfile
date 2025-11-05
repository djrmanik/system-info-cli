FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libssl-dev build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py cli_utils.py ./
COPY tests tests

ENTRYPOINT ["python", "main.py"]

CMD ["show"]
