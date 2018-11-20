# **V**isual **E**xtractor, **NO** **M**iru (VENOM)

## Usage
### セットアップ
#### 1.前準備

- 必要な環境
  - Docker
  [インストール方法](https://qiita.com/kurkuru/items/127fa99ef5b2f0288b81)

- モデルの準備
モデルファイルは[こちら](https://drive.google.com/open?id=1AdhNgIvUzsWsvUN7BQ2SITThhHW7lCsc)から取得したものを,`models/YOLOv3/models`に配置する．最終的なファイル構造は以下の形．

```ファイル構造
.
|
| - models
|     | - YOLOv3
|          | - models
|                | - coco_classes.txt
|                | - yolo_anchors.txt
|                | - yolo.h5
| - opt
〜〜~ 省略 〜〜〜

```

#### 2.Dockerによる環境構築
以下のコマンドからDockerの環境構築が行われる．

```sh:
$ make run
```

### 実行
Docker内で実行を行う．

```sh:
$ make in # コンテナにログイン
```

`./src`と`./result`フォルダが共有されている．実験用の動画は`./src`フォルダに入れる．`./results/{保存するディレクトリ名}`には実験結果が出力される．

```sh:
$ python main.py --movie_path={YouTubeのURLまたは動画のパス} --save_path={保存するディレクトリ名}
```
