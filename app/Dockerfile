FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
#/codeディレクトリ作成
RUN mkdir /code
#uwsgiログファイル作成
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
# 各種命令実行のカレントディレクトリを指定
WORKDIR /code
# ローカルのrequirements.txtをコンテナ内の/code/にコピー
ADD requirements.txt /code/
# コマンド実行
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /code/