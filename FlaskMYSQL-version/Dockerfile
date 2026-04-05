FROM python:3.8-slim
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
COPY . .

    
RUN pip install flask mysqlclient  

EXPOSE 5005
CMD ["python","app.py"]