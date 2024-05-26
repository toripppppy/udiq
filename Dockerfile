FROM python:3.11

WORKDIR /app

# 必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev

# パッケージのアップグレードと依存関係のインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ソースコードのコピー
COPY . .

# コンテナ起動時のデフォルトのコマンドを指定
CMD [ "python", "main.py"]
