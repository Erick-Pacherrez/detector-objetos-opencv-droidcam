import cv2

cap = cv2.VideoCapture("http:/192.168.1.41:4747/video")

GuantesClassif = cv2.CascadeClassifier('cascade.xml')

while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guantes = GuantesClassif.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors= 50,
        minSize=(40, 40)
    )

    for (x, y, w, h) in guantes:
        margen_x = int(w * 0.40)
        margen_y = int(h * 0.40)

        x1 = max(x - margen_x, 0)
        y1 = max(y - margen_y, 0)
        x2 = x + w + margen_x
        y2 = y + h + margen_y

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)  # Rectángulo amarillo
        cv2.putText(
            frame, 'Guantes', (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA
        )

    cv2.imshow('Deteccion - Guantes', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
