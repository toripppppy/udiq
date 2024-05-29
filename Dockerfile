FROM python:3.11

WORKDIR /app

# install packages
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
