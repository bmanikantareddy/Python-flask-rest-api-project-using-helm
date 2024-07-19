FROM python:3.8

WORKDIR /app

COPY . /app

# Install virtualenv
RUN pip install --no-cache-dir virtualenv

# Create a virtual environment
RUN virtualenv venv

# Activate the virtual environment and install dependencies
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Set the virtual environment as the default Python environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD ["python", "main.py"]
