import cv2
import os

# Obtener la ruta exacta de la carpeta actual donde está este script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Unir esa ruta con el nombre de cada archivo XML
path_casco = os.path.join(current_dir, "cascade_casco.xml")
path_chaleco = os.path.join(current_dir, "cascade_chaleco.xml")

# Verificamos si ahora sí los encuentra
print("¿Existe casco?", os.path.exists(path_casco))
print("¿Existe chaleco?", os.path.exists(path_chaleco))

# Cargar clasificadores con sus rutas completas calculadas
casco_classifier = cv2.CascadeClassifier(path_casco)
chaleco_classifier = cv2.CascadeClassifier(path_chaleco)

# Conexión a DroidCam
cap = cv2.VideoCapture("http://192.168.1.41:4747/video")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir video de la cámara.")
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detección de Casco (Verde)
    cascos = casco_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))
    for (x, y, w, h) in cascos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Casco', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
        
    # Detección de Chaleco (Azul)
    chalecos = chaleco_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6, minSize=(50, 50))
    for (x, y, w, h) in chalecos:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, 'Chaleco', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
        

    cv2.imshow('Deteccion EPP Completa', frame)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
