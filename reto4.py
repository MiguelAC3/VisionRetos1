import cv2
import numpy as np


# Abrir cámara
camara = cv2.VideoCapture(0)


# Colores que vamos a detectar
colores = {

    "ROJO": (
        np.array([0, 100, 100]),
        np.array([10, 255, 255])
    ),

    "VERDE": (
        np.array([35, 100, 100]),
        np.array([85, 255, 255])
    ),

    "AZUL": (
        np.array([90, 100, 100]),
        np.array([130, 255, 255])
    )
}


while True:

    # Capturar frame
    ret, frame = camara.read()

    if not ret:
        print("No se pudo acceder a la cámara")
        break


    # Convertir de BGR a HSV
    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )


    # Revisar cada color
    for nombre, (bajo, alto) in colores.items():

        # Crear máscara
        mascara = cv2.inRange(
            hsv,
            bajo,
            alto
        )


        # Buscar contornos
        contornos, _ = cv2.findContours(
            mascara,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )


        # Si no encontró nada
        if len(contornos) == 0:
            continue


        # Tomar el contorno más grande
        contorno = max(
            contornos,
            key=cv2.contourArea
        )


        # Calcular área
        area = cv2.contourArea(contorno)


        # Ignorar objetos demasiado pequeños
        if area < 500:
            continue


        # Obtener bounding box
        x, y, w, h = cv2.boundingRect(contorno)


        # Dibujar rectángulo
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )


        # Mostrar nombre del color
        cv2.putText(
            frame,
            nombre,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


    # Mostrar resultado
    cv2.imshow(
        "Seguimiento de figura",
        frame
    )


    # Salir con Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Liberar cámara
camara.release()

# Cerrar ventanas
cv2.destroyAllWindows()