FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 9001

CMD ["./venv/bin/python", "main.py"]
