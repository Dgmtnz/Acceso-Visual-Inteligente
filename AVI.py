import os
import cv2
import numpy as np
import time
import replicate
import base64
import pyttsx3

# Define tu token de API de Replicate
os.environ["REPLICATE_API_TOKEN"] = "tu_token_aquí"

# Inicializa la cámara
cap = cv2.VideoCapture(0)

# Inicializa el motor de text-to-speech
engine = pyttsx3.init()

while True:
    # Captura el marco de la cámara
    ret, frame = cap.read()

    # Muestra el marco en una ventana
    cv2.imshow('Webcam', frame)

    # Espera a que se presione la tecla Enter (tecla 13)
    if cv2.waitKey(1) == 13:
        # Guarda la imagen con el nombre 'foto.jpg'
        img_name = 'foto.jpg'
        cv2.imwrite(img_name, frame)

        # Codifica la imagen en base64
        with open(img_name, 'rb') as f:
            encoded_image = base64.b64encode(f.read()).decode('utf-8')

        # Aquí es donde enviarías la imagen a la API de Replicate
        input = {
            "image": "data:image/jpg;base64," + encoded_image,  # Pasa la imagen como un data URL
            "prompt": "Describe esta imagen en español, empieza a describirla con \"Veo\"",
            "max_tokens": 512
        }

        output = replicate.run(
            "yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb",
            input=input
        )

        description = "".join(output)
        print(description)

        # Lee la descripción con el text-to-speech
        engine.say(description)
        engine.runAndWait()

    # Cierra el programa si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la cámara y cierra todas las ventanas
cap.release()
cv2.destroyAllWindows()
