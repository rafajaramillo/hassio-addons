FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY run.sh .

RUN chmod +x run.sh
CMD ["./run.sh"]
