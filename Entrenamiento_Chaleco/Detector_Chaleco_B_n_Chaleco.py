import cv2
import numpy as np
import imutils
import os
import time

Datos = "n"              #Crear_carpeta_Denominada_n (Negativo para el casco)
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture("http://192.168.1.41:4747/video") #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 120, 40
x2, y2 = 600, 480

count = 0
max_imagenes = 400       # Límite máximo de fotos
tiempo_espera = 0.1      # Intervalo de tiempo en segundos
capturando = False       # Bandera para saber si debe empezar a tomar fotos

print("Presiona la tecla 'E' en la ventana del video para comenzar la captura.")

while True:

    ret, frame = cap.read()
    if not ret: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = cv2.resize(objeto, (200, 200), interpolation=cv2.INTER_CUBIC)

    k = cv2.waitKey(1)

    # Si presionas 'e' o 'E', se activa la captura
    if k == ord('e') or k == ord('E'):
        capturando = True
        ultimo_tiempo = time.time()
        print("¡Capturando fotos automáticamente...")

    # Si la bandera de captura está activa, toma fotos cada 0.5 segundos hasta llegar a 400
    if capturando:
        tiempo_actual = time.time()
        if (tiempo_actual - ultimo_tiempo) >= tiempo_espera:
            if count < max_imagenes:
                cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count), objeto)
                print('Imagen guardada [{}/{}]: '.format(count+1, max_imagenes) + Datos+'/objeto_{}.jpg'.format(count))
                count = count + 1
                ultimo_tiempo = tiempo_actual
            else:
                print("¡Proceso finalizado! Se han tomado las 400 fotos.")
                break

    # Presiona ESC (tecla 27) para salir en cualquier momento
    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()
