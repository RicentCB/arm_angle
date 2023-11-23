import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import math
import matplotlib.pyplot as plt
import time

cap = cv2.VideoCapture(1)  # Abre la cámara
# Inicializar el detector de manos
detector = HandDetector(staticMode=False,
                        detectionCon=0.7,
                        maxHands=1,
                        modelComplexity=1,
                        minTrackCon=0.5)


# Variables para el seguimiento del tiempo
start_time = time.time()
interval = 3  # Intervalo de 3 segundos
angle_list = []  # Lista para almacenar los ángulos
time_list = []  # Lista para almacenar el tiempo
numberIntervals = 0;
plt.ylim(0, 180)  # Establece el rango del eje Y

while True:
    success, img = cap.read()  # Lee el cuadro de la cámara

    hands, img = detector.findHands(img, draw=False, flipType=True)  # Encuentra las manos en la imagen

    if hands:  # Si se detectan manos
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # Lista de puntos de referencia de la mano 1
        bbbox1 = hand1["bbox"]
        center1 = hand1["center"]
        handType1 = hand1["type"]

        # Dibuja líneas entre los dedos
        x1, y1, _, _ = bbbox1
        cvzone.cornerRect(img, (x1, y1, 200, 200), l=30, t=5, rt=1, colorR=(255, 0, 255), colorC=(0, 255, 0))

        # Coordenadas de los puntos de referencia
        x1, y1 = lmList1[2][0:2] # Base pulgar
        x2, y2 = lmList1[4][0:2] # Punta Pulgar
        x3, y3 = lmList1[8][0:2] # Punta Indice

        # Calcular longitudes de lados
        a = math.dist((x1, y1), (x3, y3))
        b = math.dist((x1, y1), (x2, y2))
        c = math.dist((x2, y2), (x3, y3))

        # Calcular el ángulo
        angle_rad = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        angle_deg = math.degrees(angle_rad)

        # Lineas
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv2.line(img, (x1, y1), (x3, y3), (255, 0, 0), 3)


        # Muestra el ángulo en la pantalla
        cv2.putText(img, f'{int(angle_deg)}'+' °', (x1,y1 + 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        
        # Si han pasado el intervalo declarado, toma una muestra y agrega a las listas
        if time.time() - start_time > interval:
            start_time = time.time()  # Ajusta el inicio del siguiente intervalo
            numberIntervals += (1 * interval)

            # Agrega el ángulo y el tiempo actual a las listas
            angle_list.append(angle_deg)
            time_list.append(numberIntervals)

            # Graficar los datos
            plt.plot(time_list, angle_list, marker='o')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Ángulo (°)')
            plt.title('Seguimiento del ángulo a lo largo del tiempo')
            plt.grid(True)
            plt.pause(0.1)  # Actualiza la gráfica

    # Muestra la imagen en la ventana
    cv2.imshow("Image", img)

    # Sale del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
