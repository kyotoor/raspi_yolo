# I wrote with supporitng from the copilot

import cv2
import numpy as np

cfg_path = "yolov4-tiny.cfg"
weights_path = "yolov4-tiny.weights"
names_path = "coco.names"

# クラス名を読み込む
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

# モデルをロード
net = cv2.dnn.readNetFromDarknet(cfg_path, weights_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# カメラ起動
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 幅
cap.set(4, 480)  # 高さ

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOの入力サイズにリサイズ
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # 出力レイヤーを取得
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

    # 推論
    detections = net.forward(output_layers)

    # バウンディングボックスを描画
    # height, width から写真を取得できます。ここを変更すると、必要な情報を取得できます。
    height, width, _ = frame.shape
    for output in detections:
        for detection in output:
            scores = detection[4:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # 信頼度しきい値
                center_x, center_y, w, h = (detection[:4] * [width, height, width, height]).astype("int")
                x, y = int(center_x - w / 2), int(center_y - h / 2)

                label = f"{classes[class_id]}: {confidence:.2f}"
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("YOLO Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
