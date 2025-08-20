import cv2

# カメラを起動（通常0が内蔵カメラ）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラが開けませんでした")
    exit()

while True:
    # フレームを読み込む
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした")
        break

    # 画面に表示
    cv2.imshow('Camera', frame)

    # qキーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 解放
cap.release()
cv2.destroyAllWindows()
