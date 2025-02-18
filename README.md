# Rapberry Pi にYOLOv4を導入してリアルタイム検出
どこでもみるような実装ですが、バージョンの競合なのか上手くいかなく苦戦したので、自分が成功した例で紹介します。使用したラズパイの藻モデルは4Bです。

## カメラの設定
カメラを差し込みます。GUI操作でカメラをONにします。
最新のRasbianでカメラの設定が容易にできないのは、このような理由かと思います。https://koto-ictclub.net/20240702zerocamera/

## 環境の構築
### OSの導入
2024年の最新Rasbianでは上手くいかなかったので、Older VersionのRasbianを使用します。イメージファイルは[ここ](https://downloads.raspberrypi.org/raspbian_full/images/)から入手できます。これをRaspberry Pi Imagerを用いてブートローダーを作成します。初期設定は特にこだわりませんが、場所と言語の設定

比較的新しいRaspiのモデルはFirmwareのバージョンのせいで、古いOSを許してくれません。その場合は、最新のRasbianを入れて諦めるか、他の誘導サイトを参考に自力で頑張ってみてください。いまだに解決策がわかりません。

### aptパッケージの管理
```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install libopencv-dev libopencv-core-dev python3-opencv libopencv-contrib-dev opencv-data
```

### pipパッケージの管理とクローン
```bash
$ python3 -m venv yolo
$ (yolo) source yolo/bin/activate
$ (yolo) git clone
```

### YOLOv４の導入 
YOLOの学習済み重みファイルの導入とラベルの導入. フォルダの作成とかパスの設定は自分で適切なようにしてください
```bash
wget https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

### Run




