FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py FLASK_ENV=production
EXPOSE 5000
CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]
