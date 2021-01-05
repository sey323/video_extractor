FROM python:3.6

# opencv-devのインストール
RUN apt-get update -y && apt-get install -y libopencv-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 関連ライブラリのインストール
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Darkflowのインストール
RUN mkdir -p ~/tmp && cd ~/tmp \
    && git clone https://github.com/thtrieu/darkflow.git \
    && pip install ./darkflow \
    && rm -r ~/tmp/darkflow

# 実行環境の準備
ENV APP_NAME video-yolo
WORKDIR /home/$APP_NAME
COPY ./venders ./venders
COPY ./models ./models
COPY ./src ./src
COPY main.py .
COPY api.py .

CMD [ "python", "./api.py" ]
