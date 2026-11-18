import cv2

cap = cv2.VideoCapture("http://192.168.1.41:4747/video")

ChalecoClassif = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    chalecos = ChalecoClassif.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(30, 30)
    )

    for (x, y, w, h) in chalecos:
        margen_x = int(w * 0.30)
        margen_y = int(h * 0.30)

        x1 = max(x - margen_x, 0)
        y1 = max(y - margen_y, 0)
        x2 = x + w + margen_x
        y2 = y + h + margen_y

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Rectángulo rojo
        cv2.putText(
            frame, 'Chaleco', (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA
        )

    cv2.imshow('Deteccion - Chaleco', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
