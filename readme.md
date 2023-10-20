#Proyecto de Detección de Ángulo
Este proyecto utiliza las bibliotecas OpenCV y cvzone para detectar el ángulo entre dos dedos en una mano cerrada con forma de puño y solo dos dedos abiertos.

Instalación
Para instalar las dependencias necesarias, asegúrate de tener Python y pip instalados en tu sistema. A continuación, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```
Este comando instalará las bibliotecas necesarias: OpenCV y cvzone.
Cómo ejecutar el proyecto
Asegúrate de tener una cámara conectada a tu dispositivo.

Ejecuta el archivo main.py:

```bash
py handle_angle.py
```
Esto abrirá la cámara y comenzará a detectar los ángulos entre los dedos en tiempo real.

##Funcionamiento del proyecto
El proyecto utiliza la librería cvzone para detectar las manos en el cuadro de la cámara. Luego, verifica si los dedos índice y medio están abiertos o cerrados. Si están abiertos, dibuja una línea entre ellos y calcula el ángulo entre ellos utilizando la ley de cosenos.

El ángulo calculado se muestra en la ventana de visualización y en las líneas que conectan los dedos.