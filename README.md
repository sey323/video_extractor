# **V**isual **E**xtractor, **NO**t need I extract from **M**ovie (VENOM)

## Usage
### セットアップ
モデルファイルは[こちら](https://drive.google.com/open?id=1AdhNgIvUzsWsvUN7BQ2SITThhHW7lCsc)から取得したものを,`models/YOLOv3/models`に配置する．


```sh:
$ make run
```

### 実行
Docker内で実行を行う．

```sh:
$ make in # コンテナにログイン
```

実行コマンドは以下の通り．results/{保存するディレクトリ名}に実験結果が出力される．

```sh:
$ python main.py --movie_path={YouTubeのURLまたは動画のパス} --save_path={保存するディレクトリ名}
```
