# Rapberry Pi にYOLOv4を導入してリアルタイム検出
どこでもみるような実装ですが、バージョンの競合なのか上手くいかなく苦戦したので、自分が成功した例で紹介します。使用したラズパイの藻モデルは4Bです。

## カメラの設定
カメラを差し込みます。GUI操作でカメラをONにします。
最新のRasbianでカメラの設定が容易にできないのは、このような理由かと思います。https://koto-ictclub.net/20240702zerocamera/

## 環境の構築
### OSの用意
2024年の最新Rasbianでは上手くいかなかったので、Older Version(raspbian_full-2020-02-14/)のRasbianを使用します。イメージファイルは[ここ](https://downloads.raspberrypi.org/raspbian_full/images/)から入手できます。これをRaspberry Pi Imagerを用いてブートローダーを作成します。初期設定は特にこだわりませんが、場所と言語の設定で「Use English」をONにすることをお勧めします。

比較的新しいRaspiのモデルはFirmwareのバージョンのせいで、古いOSを許してくれません。その場合は、最新のRasbianを入れて諦めるか、他の誘導サイトを参考に自力で頑張ってみてください。いまだに解決策がわかりません。

### aptパッケージの管理
```bash
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install libopencv-dev libopencv-core-dev python3-opencv libopencv-contrib-dev opencv-data
```

### pipパッケージの管理とクローン
python-opencvはいらないかもしれない...
```bash
$ python3 -m venv yolo
$ (yolo) source yolo/bin/activate
$ (yolo) pip3 install python-opencv
$ (yolo) git clone https://github.com/kyotoor/raspi_yolo.git
```

### YOLOv４の導入 
YOLOの学習済み重みファイル、ラベルと動作設定ファイルをダウンロードします。. フォルダの作成とかパスの設定は自分で適当に設定してください。デフォルトでは、同フォルダ直下に配置しています。
```bash
wget https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights
wget https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names
```

### Run
moniterについては作成中です。検出した異常な物体を保存するプログラムを作成します。detectionで検出ボックスがでてきて、リアルタイム検出ができます。フレームレートはかなり低いですが、、、。
$ (yolo) python3 detection.py





