# ベースイメージを指定
FROM node:10.10-slim

# ディレクトリを移動する
ADD ./ /edward
WORKDIR /edward

RUN npm install

# ポート3000番を開放する
EXPOSE 3000

CMD node app.js
