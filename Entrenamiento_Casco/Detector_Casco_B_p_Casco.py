import cv2
import numpy as np
import imutils
import os
import time

Datos = "p_casco"              #Crear_carpeta_Denominada_p (Positivo)
if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture("http://192.168.1.41:4747/video") #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

x1, y1 = 120, 40
x2, y2 = 600, 480

count = 0
max_imagenes = 150       # Límite ajustado a 150 fotos positivas
tiempo_espera = 0.2      # Intervalo de 0.2 segundos
capturando = False       # Bandera para esperar la tecla 'e'

print("Presiona la tecla 'e' en la ventana del video para comenzar la captura automática.")

while True:

    ret, frame = cap.read()
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = cv2.resize(objeto, (200, 200), interpolation=cv2.INTER_CUBIC)
    #print(objeto.shape)

    k = cv2.waitKey(1)

    # Iniciar captura al presionar 'e' o 'E'
    if k == ord('e') or k == ord('E'):
        capturando = True
        ultimo_tiempo = time.time()
        print("¡Iniciando captura automática de positivas...")

    # Guardado automático cada 0.2 segundos hasta llegar a 150
    if capturando:
        tiempo_actual = time.time()
        if (tiempo_actual - ultimo_tiempo) >= tiempo_espera:
            if count < max_imagenes:
                cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count), objeto)
                print('Imagen guardada [{}/{}]: '.format(count+1, max_imagenes) + Datos+'/objeto_{}.jpg'.format(count))
                count = count + 1
                ultimo_tiempo = tiempo_actual
            else:
                print("¡Proceso finalizado! Se han tomado las 150 fotos positivas.")
                break

    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

cap.release()
cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
