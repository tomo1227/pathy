FROM python:3.10.6
ENV PYTHONUNBUFFERED 1
#/codeディレクトリ作成
#uwsgiログファイル作成
RUN mkdir -p /var/log/uwsgi/ && touch uwsgi.log
# 各種命令実行のカレントディレクトリを指定
WORKDIR /opt/pathy/
# ローカルのrequirements.txtをコンテナ内の/code/にコピー
ADD requirements.txt /opt/pathy/
# コマンド実行
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /opt/pathy/