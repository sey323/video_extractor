FROM python:3.6

# 関連ライブラリのインストール
ADD requirements.txt .
RUN pip install -r requirements.txt

# 実行環境の準備
ENV APP_NAME angelo
WORKDIR /home/$APP_NAME
COPY . .

CMD [ "python", "./run.py" ]
