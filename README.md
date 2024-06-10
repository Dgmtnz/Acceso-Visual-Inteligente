# Acceso Visual Inteligente con Llama 3

Este proyecto utiliza la API de Replicate y el modelo de inteligencia artificial Llama 3 Vision para describir imágenes capturadas en tiempo real desde una cámara web. La descripción de la imagen se genera en español y se lee en voz alta utilizando un motor de text-to-speech. El objetivo principal es mejorar la accesibilidad, permitiendo a las personas con discapacidades visuales entender su entorno a través de descripciones de audio.

## Requisitos

- Python 3.6 o superior
- OpenCV
- Numpy
- Replicate
- Pyttsx3

## Configuración

Primero, debes definir tu token de API de Replicate en tu entorno:

```python
os.environ["REPLICATE_API_TOKEN"] = "tu_token_aquí"
```

## Uso

El script principal del proyecto es `AVI.py`. Al ejecutarlo, se inicializa la cámara y el motor de text-to-speech. Luego, entra en un bucle infinito donde captura un marco de la cámara y lo muestra en una ventana.

Si presionas la tecla Enter, el marco actual se guarda como ‘foto.jpg’, se codifica en base64 y se envía a la API de Replicate utilizando el modelo Llama 3 Vision. La API devuelve una descripción de la imagen, que se imprime en la consola y se lee en voz alta.

Para salir del programa, presiona la tecla ‘q’. //no va

## Licencia

Este proyecto está bajo la licencia GNU General Public License (GPL).

Espero que esto te sea útil. Si tienes alguna pregunta o sugerencia, no dudes en preguntar. ¡Muchas gracias!
