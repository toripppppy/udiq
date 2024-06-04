# Udiq
Ubiquitous-Dictionaryの略。会話中の専門用語に補足を加えるDiscord Botです。<br>
ユビキタスな会話を実現しよう！

![うごいてる](https://github.com/toripppppy/udiq/assets/96613082/268c149a-d089-4b66-8318-1023d4860256)

（現在ベータ版で、動作が不安定なので公開はしていないです。興味がある方は声をかけてください。）

# 環境構築
Discord.pyで作ってます。<br>
EC2上でdocker-composeでMariaDBとPythonのDockerを建てて動かしている構成です。

まず、Discord Developer Portalでbotを作成してTokenを控えておいてください。<br>
git cloneして、以下のように`/.env`を作成
```
# TOKEN
TOKEN="XXXXXXXXXXXXXXXXXXX"

# CHANNELS
LOG_CHANNEL_ID="000000000000000000"

# MariaDB
DB_USER="user"
DB_PASSWORD="pass"
MARIADB_ROOT_PASSWORD="pass"
```
docker-composeで起動
```
$ docker-compose build
# docker-compose up -d
```

PRお待ちしてますーー
