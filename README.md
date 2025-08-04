# Descargador de Videos

Este es un sencillo script de Python para descargar videos de diversas páginas web utilizando `yt-dlp`.

## Requisitos

- Python 3.6 o superior. Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

## Instalación

1.  **Clona o descarga este repositorio.**

2.  **Abre una terminal o línea de comandos** en la carpeta del proyecto.

3.  **Instala las dependencias necesarias:**

    ```bash
    pip install -r requirements.txt
    ```

    *Nota sobre el entorno virtual:* Aunque no es estrictamente necesario para que funcione, se recomienda instalar las dependencias en un [entorno virtual](https://docs.python.org/es/3/tutorial/venv.html) para evitar conflictos con otros proyectos de Python.

## Uso

Para descargar un video, ejecuta el script `downloader.py` desde tu terminal, pasándole la URL de la página del video como argumento.

```bash
python downloader.py "URL_DEL_VIDEO_AQUI"
```

**Ejemplo:**

```bash
python downloader.py "https://www.ejemplo.com/video/12345"
```

El video se descargará en una carpeta llamada `downloads` dentro del directorio del proyecto.

## ¿Cómo funciona?

El script utiliza la potente biblioteca `yt-dlp`, que se encarga de analizar la página, encontrar el flujo de video principal (ignorando anuncios y miniaturas) y descargarlo en la mejor calidad disponible en formato MP4.
