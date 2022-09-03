FROM node:18-buster-slim
 
# 開発ディレクトリ設定
WORKDIR /code
# COPY ./package*.json ${WORKDIR}/

#  # コンテナ内でパッケージを一括インストール
RUN npm update npm && npm install -g @vue/cli && \
    npm install -g @vue/cli-init 

COPY . ${WORKDIR}/