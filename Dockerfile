FROM python:3.9-slim
RUN apt-get update && \
    apt-get install -y gcc python3-dev && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV SOLARA_APP=sol.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8765"]