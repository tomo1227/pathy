FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

#開発ディレクトリ作成
ENV WORKDIR /opt/pathy

#uwsgiログファイル作成
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
# 各種命令実行のカレントディレクトリを指定
WORKDIR ${WORKDIR}
# ローカルのrequirements.txtをコンテナ内のにコピー
COPY requirements.txt ${WORKDIR}
# コマンド実行
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
COPY . ${WORKDIR}/