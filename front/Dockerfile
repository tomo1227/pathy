FROM node:18-buster-slim
 
# 開発ディレクトリ設定
WORKDIR /code
COPY ./package*.json ${WORKDIR}/

RUN npm update npm
RUN npm ci
RUN npm install -g @vue/cli && \
    npm install -g @vue/cli-init

# RUN npm install axios
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
COPY . ${WORKDIR}/