# **V**isual **E**xtractor, **NO** **M**iru (VENOM)
# 概要
Youtubeの動画に対してYOLOによる物体検出を行うプログラムである。
出力結果をcsvとexelで確認できる。

# 利用方法
## 環境構築
以下のどちらかの環境が用意されている必要がある。

- Docker  
- Python（ver3.8を推奨）


### 1. 学習済み重みのダウンロード
物体検出を行う際に利用する、YOLOの学習済み重みファイルをダウンロードする。[こちら](https://drive.google.com/open?id=1AdhNgIvUzsWsvUN7BQ2SITThhHW7lCsc)から取得した学習済み重みを、`models/YOLO_small/`に配置する。

```ファイル構造
./video-yolo
|
| - models
|     | - YOLO_small
|           | - YOLO_small_tf.py
|           | - YOLO_small.ckpt ←ここに配置する
| - opt
〜〜~ 省略 〜〜〜

```

### 2. 環境構築
本プロジェクトは、Dockerによる環境構築、Pythonによる環境構築のどちらかで環境を構築することができる。

### 2-A. Dockerによる環境構築
Dockerを用いて環境構築を行う場合は、以下のコマンドを実行する。

```sh:
$ make run
```

コンテナとは、ソースコードの実態である`./src`と、処理結果が保存される`./result`フォルダが共有されている。コンテナの起動後、以下のコマンドでコンテナにログインし、各種処理を行う。

```sh:
$ make in
```


### 2-B. Pythonによる環境構築
ローカルにPython環境がある場合は、以下のコマンドで依存ライブラリをインストールする。

```sh:
$ pip install -r requiremente.txt
```

その後、darknetのインストールを行う。

```sh:
$ mkdir -p build
$ cd build 
$ git clone https://github.com/thtrieu/darkflow.git
$ pip install ./darkflow
```


## 実行
### コンソールで処理を実行する場合
python cliを利用して処理を実行する場合は、以下のコマンドを用いる。処理結果は`./results/${保存するディレクトリ名}`に保存される。

```sh:
$ python main.py --movie_path=${YouTubeのURLまたは動画のパス} \
                 --save_path=${保存するディレクトリ名}
```

### APIサーバを立てて、API経由で実行する場合
APIサーバを立てて、外部から処理を実行することができる。APIサーバを実行する場合、以下のコマンドを用いる。

```sh
$ python api.py
```

`localhost:3000`に対してリクエストを送ることで、API経由で処理を実行することができる。